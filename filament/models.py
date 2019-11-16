import os

from django.db import models
from django.db.models import Q
from django.db.models.signals import post_delete
from django.dispatch import receiver
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
FILAMENT_MATERIAL_CHOICES = (
    ( 'PLA', 'PLA' ),
    ( 'ABS', 'ABS' ),
    ( 'TPU', 'TPU' ),
)

def getext(filename):
    _, ext = os.path.splitext(filename)
    if len(ext) == 0:
        return '.png'
    return ext

FILAMENT_IMAGE_DIR = 'filament_images'
def get_filament_image_upload_path(instance, filename):
    return os.path.join(FILAMENT_IMAGE_DIR, '%d%s' % (instance.id, getext(filename)))

# to use primary key(id) in FileField(upload_to=XXX)
# https://stackoverflow.com/questions/9968532/django-admin-file-upload-with-current-model-id
def upload_save(func):
    def wrapper(*args, **kwargs):
        self = args[0]

        if self.id is None:
            saved = []
            for f in self.__class__._meta.get_fields():
                if isinstance(f, models.FileField):
                    saved.append((f.name, getattr(self, f.name)))
                    setattr(self, f.name, None)

            func(*args, **kwargs)

            for name, val in saved:
                setattr(self, name, val)
        func(*args, **kwargs)

    return wrapper

class Filament(models.Model):
    material = models.TextField(choices=FILAMENT_MATERIAL_CHOICES)
    amount = models.FloatField()
    price = models.IntegerField()
    shop = models.TextField()
    url = models.URLField()
    owner = models.TextField()
    name = models.TextField()

    image_file = models.ImageField(upload_to=get_filament_image_upload_path, null=True)
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

@receiver(post_delete, sender=Filament)
def after_delete_filament(sender, instance, **kwargs):
    instance.image_file.delete(False)
