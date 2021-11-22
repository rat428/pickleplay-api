from django.db import models

# Create your models here.
from django.db import models
import uuid
from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from faker import Faker
from faker.providers import geo
fake = Faker()
fake.add_provider(geo)


class Photo(models.Model):
    objects = models.Manager()

    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()

    @staticmethod
    def generate_random():
        p = Photo.objects.create()
        # image_url = fake.image_url()
        # img_temp = NamedTemporaryFile(delete=True)
        # img_temp.write(urlopen(image_url).read())
        # img_temp.flush()
        p.photo = fake.image_url()
        p.save()
        return p


