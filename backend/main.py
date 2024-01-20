from tesserocr import PyTessBaseAPI
import os
import preprocessing as pp

img_path = "images/grace.jpg"

# Get image

img_path = pp.preprocessing_cv2(img_path)

with PyTessBaseAPI(path="tessdata_best") as api:
    api.SetImageFile(img_path)
    text = api.GetUTF8Text()
    print(text)
    print(len(text))
    print(api.AllWordConfidences())

# api is automatically finalized when used in a with-statement (context manager).
# otherwise api.End() should be explicitly called when it's no longer needed.
