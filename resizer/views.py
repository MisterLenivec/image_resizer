from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Picture
from .forms import PictureCreateFrom, PictureResizeForm
from .service import images_resize


class PicturesView(ListView):
    """Image list"""
    model = Picture
    queryset = Picture.objects.all()
    template_name = 'resizer/picture_list.html'


class PictureCreate(CreateView):
    """Upload an image"""
    model = Picture
    form_class = PictureCreateFrom
    template_name = 'resizer/picture_create.html'


class PictureDetail(DetailView):
    """Image view and resizing"""
    model = Picture
    form_class = PictureResizeForm
    template_name = 'resizer/picture_detail.html'

    @staticmethod
    def post(request, pk, *args, **kwargs):
        picture = Picture.objects.get(id=pk)
        form = PictureResizeForm(request.POST, instance=picture)
        if form.is_valid():
            width = form.cleaned_data.get('width')
            height = form.cleaned_data.get('height')
            name = form.cleaned_data.get('image_file')
            picture = images_resize(name, width, height)
            picture.id = pk
            form.save()
            context = {'form': form, 'picture': picture}
            return render(request, 'resizer/picture_detail.html', context)

        context = {'form': form, 'picture': picture}
        return render(request, 'resizer/picture_detail.html', context)
