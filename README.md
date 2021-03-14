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
```
```python
# Search Web Image by text
# You can use Chinese or English
photo_urls = imsp_engine.im_search('sky')
```
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
<img src="https://unsplash.com/photos/pnvA8iLJcDI/download?w=224"/>

Original image：<a target="_blank" href="https://unsplash.com/photos/pnvA8iLJcDI">Unsplash Link</a> 

<img src="https://unsplash.com/photos/fBn-JJk_V_w/download?w=224"/>

Original image：<a target="_blank" href="https://unsplash.com/photos/fBn-JJk_V_w">Unsplash Link</a> 

<img src="https://unsplash.com/photos/7YFfGE26kbs/download?w=224"/>

Original image：<a target="_blank" href="https://unsplash.com/photos/7YFfGE26kbs">Unsplash Link</a> 