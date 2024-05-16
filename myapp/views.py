from django.shortcuts import render
from . forms import ImageForm
from . models import Image

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    img = Image.objects.all()
    form = ImageForm()
    context = {'form':form, 'img':img}
    return render(request,'myapp/home.html', context)
