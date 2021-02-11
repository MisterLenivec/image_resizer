from django.db import models
from django.core.files import File
from django.urls import reverse
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
import uuid


class Picture(models.Model):
    """Picture model"""
    image_file = models.ImageField(upload_to='', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image_url and not self.image_file:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            val = None
            for i in ['.png', '.jpeg', '.jpg', '.svg', '.gif']:
                if i in self.image_url.lower():
                    val = i
            if val is None:
                val = '.png'
            self.image_file.save(f"image_{uuid.uuid4()}{val}", File(img_temp))
        super(Picture, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('picture_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['-id']
