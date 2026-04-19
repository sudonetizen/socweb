from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import ImageCreateForm
from .models import Image


class ImageCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ImageCreateForm(data=request.GET)
        return render(request, 'img_create.html', {'section':'images', 'form':form}) 

    def post(self, request):
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()

            messages.success(request, 'Image added successfully')
            
            return redirect(new_image.get_absolute_url())

        return render(request, 'img_create.html', {'section':'images', 'form':form}) 


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'img_detail.html', {'section':'images', 'image': image})

