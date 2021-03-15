# Paddle-IMSP
![GitHub forks](https://img.shields.io/github/forks/AgentMaker/Paddle-IMSP)
![GitHub Repo stars](https://img.shields.io/github/stars/AgentMaker/Paddle-IMSP)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/AgentMaker/Paddle-IMSP?include_prereleases)
![GitHub](https://img.shields.io/github/license/AgentMaker/Paddle-IMSP)  
An Image Search and Pair system base on PaddlePaddle.

Search Web Image by text and pair similar images by image.

Base project：[【Paddle-CLIP】](https://github.com/AgentMaker/Paddle-CLIP).

## Project Information
* This project is limited to non-commercial scenarios

* All the retrieved and matched web images are from the website: [【unsplash】](https://unsplash.com/)

* If you need to use the original image, please move to [【unsplash】](https://unsplash.com/) Download

* Thanks to [【unsplash】](https://unsplash.com/data) open source large-scale image dataset

* Thanks to [【openai/CLIP】](https://github.com/openai/CLIP/) open source model code and pretrained model parameters


## Install Package
* Install by pip：
```shell
$ pip install paddleimsp
```
* Install by wheel package：[【Releases Packages】](https://github.com/AgentMaker/Paddle-IMSP/releases)

## Quick Start
```python
from imsp import IMSP

# Load the engine
# The first load will automatically download the pretrained model and images database
imsp_engine = IMSP()
```
```python
# Search Web Image by text
# You can use Chinese or English
photo_urls = imsp_engine.im_search('sky')
```
Preview photos:

<img src="https://unsplash.com/photos/OnGV9X-ql08/download?w=224"/>

Original image：<a target="_blank" href="https://unsplash.com/photos/OnGV9X-ql08">Unsplash Link</a> 

<img src="https://unsplash.com/photos/IyEwFM-fAVk/download?w=224"/>

Original image：<a target="_blank" href="https://unsplash.com/photos/IyEwFM-fAVk">Unsplash Link</a> 

<img src="https://unsplash.com/photos/7dF1FloGPpE/download?w=224"/>

Original image：<a target="_blank" href="https://unsplash.com/photos/7dF1FloGPpE">Unsplash Link</a>
```python
# Pair similar images by image
photo_urls = imsp_engine.im_pair('fruit.jpg')
```
Preview photos:

<img src="https://unsplash.com/photos/pnvA8iLJcDI/download?w=224"/>

Original image：<a target="_blank" href="https://unsplash.com/photos/pnvA8iLJcDI">Unsplash Link</a> 

<img src="https://unsplash.com/photos/fBn-JJk_V_w/download?w=224"/>

Original image：<a target="_blank" href="https://unsplash.com/photos/fBn-JJk_V_w">Unsplash Link</a> 

<img src="https://unsplash.com/photos/7YFfGE26kbs/download?w=224"/>

Original image：<a target="_blank" href="https://unsplash.com/photos/7YFfGE26kbs">Unsplash Link</a> 

```python
# Use the images and texts to search and pair images
photo_urls = imsp_engine.im_search_pair(images=['road.jpg'], texts=['cars', 'peoples'], topk=5)
```
<img src="https://unsplash.com/photos/6FpUtZtjFjM/download?w=224"/>

原图请点击：<a target="_blank" href="https://unsplash.com/photos/6FpUtZtjFjM">Unsplash Link</a>

<img src="https://unsplash.com/photos/-6XDz7LiBxw/download?w=224"/>

原图请点击：<a target="_blank" href="https://unsplash.com/photos/-6XDz7LiBxw">Unsplash Link</a>

<img src="https://unsplash.com/photos/U6j3dsF_rMY/download?w=224"/>

原图请点击：<a target="_blank" href="https://unsplash.com/photos/U6j3dsF_rMY">Unsplash Link</a>