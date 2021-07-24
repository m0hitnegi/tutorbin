from django.shortcuts import render, redirect
from django.http import HttpResponse
from PIL import Image as Img
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *



def index(request):
    image = Image.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(image, 8)
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    return render(request, 'gallery/index.html', {'images': images})


def uploadimage(request):
    return render(request, 'gallery/upload.html')


def saveimage(request):
    imagefile = Image()
    imagefile.image = request.FILES['image']
    try:
        Image.objects.get(name=imagefile.image.name)
        return redirect('index')
    except:
        pass
    imagefile.name = imagefile.image.name
    imagefile.save()
    if len(request.POST['tags']):
        for i in request.POST['tags'].split(','):
            tagged = Tags.objects.get(tag=i.strip())
            tagged.img.add(imagefile)
    return redirect('index')



def showimage(request):
    current_image = request.get_full_path()[11:]
    img_obj = Image.objects.get(name=current_image)
    tags = img_obj.tags_set.all()
    if 'left' in request.POST:
        rotateleft = img_obj.image
        img = Img.open(rotateleft)
        img = img.rotate(90, expand=True)

        img.save('media/' + current_image)
        img.close()
    elif 'right' in request.POST:
        rotateleft = img_obj.image
        img = Img.open(rotateleft)
        img = Img.open('media/' + current_image)
        img = img.rotate(-90, expand=True)

        img.save('media/' + current_image)
        img.close()
    context = {'image': current_image}
    return render(request, 'gallery/showimage.html', context, )


def searchbytag(request):
    searched_tag = request.get_full_path()[5:]
    tag_obj = Tags.objects.get(tag=searched_tag)
    img_list = []
    for i in tag_obj.img.all():
        img_list.append(i.image)
    return render(request, 'gallery/search.html', {'images': img_list})


