from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Picture


class PictureCreateFrom(forms.ModelForm):
    """Image upload form"""
    class Meta:
        model = Picture
        fields = ('image_file', 'image_url')

    def clean(self):
        image_file = self.cleaned_data.get('image_file')
        image_url = self.cleaned_data.get('image_url')

        if not image_file and not image_url:
            raise forms.ValidationError(_('Одно из полей обязательно для ввода!'))
        elif image_file and image_url:
            raise forms.ValidationError(_('Максимум одно поле доступно для ввода!'))
        return self.cleaned_data


class PictureResizeForm(forms.ModelForm):
    """Image resizing form"""
    height = forms.IntegerField(label='height', min_value=0, required=False)
    width = forms.IntegerField(label='width', min_value=0, required=False)

    class Meta:
        model = Picture
        fields = ('id', 'image_file', 'image_url', 'width', 'height')

    def clean(self):
        width = self.cleaned_data.get('width')
        height = self.cleaned_data.get('height')

        if not width and not height:
            raise forms.ValidationError(_('Минимум одно поле обязательно для ввода!'))
        elif width is not None and width < 3 or height is not None and height < 3:
            raise forms.ValidationError(_('Изображение должно быть не много больше!'))
        return self.cleaned_data
