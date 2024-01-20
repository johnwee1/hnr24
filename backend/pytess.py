from tesserocr import PyTessBaseAPI
from PIL import Image
from PIL import ImageEnhance
import os

images = ["images/aminoapps.jpg"]

with PyTessBaseAPI(path="tessdata_best") as api:
    for img in images:
        api.SetImageFile(img)
        text = api.GetUTF8Text()
        print(text)
        print(len(text))
        print(api.AllWordConfidences())

# api is automatically finalized when used in a with-statement (context manager).
# otherwise api.End() should be explicitly called when it's no longer needed.
