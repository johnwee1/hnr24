from tesserocr import PyTessBaseAPI
from PIL import Image

image = "sample_4.jpeg"


def preprocess_to_grayscale(input_image_path):
    # changes images to grayscale
    # Open the image file
    original_image = Image.open(input_image_path)

    # Convert the image to grayscale
    grayscale_image = original_image.convert("L")

    # Save the preprocessed image
    grayscale_image.save(input_image_path)


preprocess_to_grayscale(image)

images = []
images.append(image)

with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        text = api.GetUTF8Text()
        print(text)
        print(len(text))
        print(api.AllWordConfidences())
# api is automatically finalized when used in a with-statement (context manager).
# otherwise api.End() should be explicitly called when it's no longer needed.
