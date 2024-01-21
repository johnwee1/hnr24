from tesserocr import PyTessBaseAPI
import os
import optical.preprocessing as pp
import optical.chatgpt as chatgpt
import numpy as np
import cv2
from PIL import Image


# Get image
def tesseract(img):
    nd_thresh = pp.preprocessing_cv2(img)
    img_thresh = Image.fromarray(nd_thresh.astype("uint8"))
    text = None
    filedir = os.path.dirname(__file__)
    filedir = os.path.join(filedir, "tessdata_best")
    with PyTessBaseAPI(path=filedir) as api:
        api.SetImage(img_thresh)
        text = api.GetUTF8Text()
        print(text)
        print(f"len={len(text)}")
        print(api.AllWordConfidences())
    if len(text) == 0:
        return "Sentence not found"
    return text


# api is automatically finalized when used in a with-statement (context manager).
# otherwise api.End() should be explicitly called when it's no longer needed.
