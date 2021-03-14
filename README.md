# Paddle-IMSP
Paddle Image Search and Pair. 

Search Web Image by text and pair similar images by image.

Base project：[【Paddle-CLIP】](https://github.com/AgentMaker/Paddle-CLIP).

## Install Package
* Install by pip：
```shell
$ pip install paddleimsp==1.0.0 -i https://pypi.python.org/pypi 
```
* Install by wheel package：[【Releases Packages】](https://github.com/AgentMaker/Paddle-IMSP/releases)

## Quick Start
```python
from imsp import IMSP

# Load the engine
imsp_engine = IMSP()

# Search Web Image by text
# You can use Chinese or English
photo_urls = imsp_engine.im_search('sky')

# Pair similar images by image
photo_urls = imsp_engine.im_pair('fruit.jpg')
```