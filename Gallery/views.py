from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import *


# Create your views here.

def Home(request):
    dict = {"images": Image.objects.all()}
    return render(request, "index.html", dict)


def Add_Images(request):
    form = Add_Image_Form()
    total_tags = Image_Tags.objects.all()
    if request.method == 'POST':
        form = Add_Image_Form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            tags = Image_Tags.objects.get(id=request.POST['tags'])
            data.tags = tags
            data.save()
            return redirect('home')
    dict = {"form": form, "tags": total_tags}
    return render(request, "add_image.html", dict)


def Show_Filter(request, status):
    image = None
    if status != 'All':
        try:
            tag = Image_Tags.objects.get(tags=status)
            image = Image.objects.filter(tags=tag)

        except:
            pass

    else:
        image = Image.objects.all()

    dict = {'images': image, 'status': status}
    return render(request, "index.html", dict)

def Open_Image(request,img_id):
    image=Image.objects.get(id=img_id)
    dict={'image':image}
    return render(request,'operation.html',dict)
