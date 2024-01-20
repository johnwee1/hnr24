from django.http import JsonResponse
import os
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
        return JsonResponse({"message": f'Form data received: {form_data}'})
        
    data = {"message": "Hello, Django!"}
    return JsonResponse(data)
