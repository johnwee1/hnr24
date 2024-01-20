from django.http import JsonResponse
import os

#####################################################################################
from tesserocr import PyTessBaseAPI
from PIL import Image
from PIL import ImageEnhance
import os

images = ["sample_7.jpeg"]


def convert_file(input_image_path):
    filepath, filename = os.path.split(input_image_path)
    filename, ext = os.path.split(filename)
    if ext == ".jpeg":
        ext = ".jpg"
    elif ext == ".png":
        image = Image.open(input_image_path).convert("RGB")
    image.save(os.path.join(filepath, f"{filename}{ext}"))


def preprocessing(input_image_path):
    # changes images to grayscale
    # Open the image file
    original_image = Image.open(input_image_path)

    # Convert the image to grayscale
    grayscale_image = original_image.convert("L")

    enhancer = ImageEnhance.Contrast(grayscale_image)

    # Adjust the contrast factor (1.0 means no change, values above 1.0 increase contrast)
    contrast_factor = 2  # You can adjust this value based on your preference
    contrast_img = enhancer.enhance(contrast_factor)

    # Save the preprocessed image
    contrast_img.save(input_image_path)

def run(img):
    path = os.path.join("../tessdata_best")
    print(path)
    with PyTessBaseAPI(path=path) as api:
        api.SetImageFile(img)
        text = api.GetUTF8Text()
        print("text:",text)
        print("text len:", len(text))
        print("confidences:", api.AllWordConfidences())
        return text
        

# api is automatically finalized when used in a with-statement (context manager).
# otherwise api.End() should be explicitly called when it's no longer needed.

################################################################################



def my_view(request):
    if request.method == 'POST':
        if request.FILES:
            print(request.FILES)
            uploaded_file = request.FILES['file']
            print("Uploaded File:", uploaded_file.name)

            # Read the content from the UploadedFile
            file_content = uploaded_file.read()
            # Specify the path where you want to save the file
            save_path = os.path.join('save.png')
            # Save the content to the new file
            with open(save_path, 'wb') as destination_file:
                destination_file.write(file_content)

        # Handle the form data here
        form_data = request.POST
        # text = run("sample_7.jpeg") #
        text = run("save.png")
        os.system("touch status.txt")
        return JsonResponse({"message": f'Form data received: {form_data}', "textIdentified" : str(text)})
        
    data = {"message": "Hello, Django!"}
    return JsonResponse(data)


def counter_check(request):
    try:
        if not os.path.exists("status.txt"):
            raise Exception("useless")
        print("readed")
        os.remove("status.txt")
        print("status delete")
        return JsonResponse({"hit": 1})
    except Exception as e:
        print("Error:", e)
        return JsonResponse({"hit": 0}, status=404)