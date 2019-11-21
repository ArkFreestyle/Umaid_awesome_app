from django.shortcuts import render, HttpResponse
from cv_app.models import Image


def main_page(request):
    """
    View for the main page:
    1) Receive an image uploaded by the user
    2) Perform image processing on the image
    3) Display the image with the result/prediction
    """

    # This if statement will work when user submits the form (presses the upload button)
    if request.method == "POST":
        # Getting image name and image inputted by user
        image_name = request.POST.get("name")
        image = request.FILES.get("image")
        
        # Creating and saving the image in SQLite database
        image_object = Image.objects.create(name=image_name, image=image)
        
        # RUN YOUR OPENCV MODEL PREDICTION FUNCTION HERE
        # Get prediction and store it in the variable below:
        image_prediction = "I am your image's prediction!!!"

        # These variables get passed to our HTML template for displaying
        context = {
        'image_name': image_name,
        'image': image,
        'image_prediction': image_prediction,
        }
    
        return render(request, 'cv_app/main_page.html', context)
    
    # This is what runs when page is normally loaded on a browser (i.e: with a GET request)
    image_prediction = 'No prediction yet'

    context = {
        'image_name': None,
        'image': None,
        'image_prediction': None,
    }
    
    return render(request, 'cv_app/main_page.html', context)