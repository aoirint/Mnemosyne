import os

from django.db import models
from django.db.models import Q
from django.db.models.signals import post_delete
from django.dispatch import receiver

from filament.models import *

# Create your models here.

PRINT3d_IMAGE_DIR = 'print3d_images'
def get_print3d_image_upload_path(instance, filename):
    return os.path.join(PRINT3d_IMAGE_DIR, '%d%s' % (instance.id, getext(filename)))

class Print3d(models.Model):
    filament = models.ForeignKey(Filament, on_delete=models.CASCADE)
    user = models.TextField()
    amount = models.FloatField()

    memo = models.TextField()

    image_file = models.ImageField(upload_to=get_print3d_image_upload_path)
    thumbnail = ImageSpecField(
        source='image_file',
        processors=[ ResizeToFill(256, 256), ],
        format='JPEG',
        options={ 'quality': 60 },
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @upload_save
    def save(self, *args, **kwargs):
        super(self.__class__, self).save(*args, **kwargs)

@receiver(post_delete, sender=Print3d)
def after_delete_print3d(sender, instance, **kwargs):
    instance.image_file.delete(False)
