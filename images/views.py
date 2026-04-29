from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse, HttpResponse
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


class ImageLikeView(LoginRequiredMixin, View):
    def post(self, request):
        image_id = request.POST.get('id')
        action = request.POST.get('action')
        if image_id and action:
            try:
                image = Image.objects.get(id=image_id)
                if action == 'like':
                    image.users_like.add(request.user)
                else:
                    image.users_like.remove(request.user)
                return JsonResponse({'status':'ok'})
            except Image.DoesNotExist:
                pass
        
        return JsonResponse({'status':'error'})


class ImageListView(LoginRequiredMixin, View):
    def get(self, request):
        images = Image.objects.all()
        paginator = Paginator(images, 8)
        page = request.GET.get('page')
        images_only = request.GET.get('images_only')

        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            if images_only:
                return HttpResponse('')
            images = paginator.page(paginator.num_pages)

        if images_only:
            return render(request, 'list_img.html', {'section':'images', 'images':images})
        return render(request, 'list_img2.html', {'section':'images', 'images':images})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'img_detail.html', {'section':'images', 'image': image})

