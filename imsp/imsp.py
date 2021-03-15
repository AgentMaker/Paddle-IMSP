import os
import time
import wget
import paddle
from PIL import Image
from .translator import Translator
from clip import tokenize, load_model


class IMSP:
    def __init__(self, db_file=None):
        self.model, self.transforms = load_model('ViT_B_32', pretrained=True)
        if db_file is None:
            db_file = 'image_db'
            db_url = 'https://bj.bcebos.com/v1/ai-studio-online/775e9601019646b2a09f717789a4602f069a26302f8643418ec7c2370b895da9?responseContentDisposition=attachment%3B%20filename%3Dimage_db'
            if not os.path.isfile(db_file):
                wget.download(db_url)
        self.image_features, self.photo_ids = self.load_db(db_file)
        self.translator = Translator()

    @staticmethod
    def load_db(db_file):
        image_db = paddle.load(db_file)

        image_features = image_db['image_features'].astype('float32')
        image_features = paddle.to_tensor(image_features)

        photo_ids = image_db['photo_ids']

        return image_features, photo_ids

    @staticmethod
    def get_urls(photo_ids):
        urls = []
        for photo_id in photo_ids:
            url = f"https://unsplash.com/photos/{photo_id}"
            urls.append(url)
        return urls

    @staticmethod
    def is_chinese(texts):
        return any('\u4e00' <= char <= '\u9fff' for char in texts)

    def im_search(self, texts, topk=5, return_urls=True):
        if self.is_chinese(texts):
            texts = self.translator.translate(texts)

        texts = tokenize(texts)
        with paddle.no_grad():
            text_features = self.model.encode_text(texts)

        logit_scale = self.model.logit_scale.exp()
        logits_per_text = logit_scale * text_features @ self.image_features.t()

        indexs = logits_per_text.topk(topk)[1][0]
        photo_ids = [self.photo_ids[index] for index in indexs]

        if return_urls:
            return self.get_urls(photo_ids)
        else:
            return photo_ids

    def im_pair(self, images, topk=5, return_urls=True):
        images = Image.open(images)
        images = self.transforms(images).unsqueeze(0)
        with paddle.no_grad():
            image_features = self.model.encode_image(images)

        logit_scale = self.model.logit_scale.exp()
        logits = logit_scale * image_features @ self.image_features.t()

        indexs = logits.topk(topk)[1][0]
        photo_ids = [self.photo_ids[index] for index in indexs]

        if return_urls:
            return self.get_urls(photo_ids)
        else:
            return photo_ids

    def im_search_pair(self, images=None, texts=None, topk=5, return_urls=True):
        if images is not None:
            if isinstance(images, list):
                input_images = []
                for image in images:
                    image = Image.open(image)
                    image = self.transforms(image).unsqueeze(0)
                    input_images.append(image)
                input_images = paddle.concat(input_images)
            elif isinstance(images, str):
                input_images = Image.open(images)
                input_images = self.transforms(input_images).unsqueeze(0)

            with paddle.no_grad():
                image_features = self.model.encode_image(input_images)

        if texts is not None:
            if isinstance(texts, list):
                input_texts = []
                for text in texts:
                    if self.is_chinese(text):
                        input_texts.append(self.translator.translate(text))
                        time.sleep(1)
                    else:
                        input_texts.append(text)
            elif isinstance(texts, str):
                if self.is_chinese(texts):
                    input_texts = self.translator.translate(texts)
                else:
                    input_texts = texts
            input_texts = tokenize(input_texts)

            with paddle.no_grad():
                text_features = self.model.encode_text(input_texts)

        if images and texts:
            features = paddle.concat([image_features, text_features], 0)
            features = paddle.sum(features, axis=0, keepdim=True)
        elif images:
            features = paddle.sum(image_features, axis=0, keepdim=True)
        elif texts:
            features = paddle.sum(text_features, axis=0, keepdim=True)

        logit_scale = self.model.logit_scale.exp()
        logits = logit_scale * features @ self.image_features.t()

        indexs = logits.topk(topk)[1][0]
        photo_ids = [self.photo_ids[index] for index in indexs]

        if return_urls:
            return self.get_urls(photo_ids)
        else:
            return photo_ids
