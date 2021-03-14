import random
import requests
from hashlib import md5


class Translator:
    def __init__(self):
        self.appid = '20210313000725566'
        self.appkey = 'anWY5DNo2Ab57bgmXnqR'
        self.url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.payload = {
            'appid': '20210313000725566',
            'from': 'zh',
            'to': 'en',
        }

    @staticmethod
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    def translate(self, query):
        salt = random.randint(32768, 65536)
        sign = self.make_md5(self.appid + query + str(salt) + self.appkey)

        self.payload['salt'] = salt
        self.payload['sign'] = sign
        self.payload['q'] = query
        r = requests.post(self.url, params=self.payload, headers=self.headers)
        result = r.json()['trans_result'][0]['dst']

        return result
