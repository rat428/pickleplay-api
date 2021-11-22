from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from faker import Faker
from faker.providers import geo
import photos.models
import random
from django.contrib.gis.geos import Point

fake = Faker()
fake.add_provider(geo)


# Create your models here.


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Court(BaseModel):
    class CourtType(models.TextChoices):
        PICKLEBALL = 'pickleball', _('Pickleball')
        TENNIS = 'tennis', _('Tennis')
        BADMINTON = 'badminton', _('Badminton')

    class PaidType(models.TextChoices):
        PAID = 'paid', _('Paid')
        FREE = 'free', _('Free')
        UNKNOWN = 'unknown', _('Unknown')

    name = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    location = models.PointField()
    types = models.CharField(choices=CourtType.choices, default=CourtType.TENNIS, max_length=50)
    buy_membership = models.BooleanField(null=True)
    num_courts = models.IntegerField()
    phone = models.CharField(blank=True, help_text='Court phone number', max_length=20)
    info = models.TextField()
    rating = models.FloatField()
    website = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)
    cost = models.CharField(choices=PaidType.choices, default=PaidType.UNKNOWN, max_length=50)
    need_membership = models.BooleanField(null=True)
    has_lighting = models.BooleanField(null=True)
    images = models.ManyToManyField(photos.models.Photo)

    @staticmethod
    def generate_random():
        random_photos = []
        for _ in range(fake.random_int(1, 5)):
            random_photos.append(photos.models.Photo.generate_random())

        latlng = fake.local_latlng(country_code='US', coords_only=True)
        print(latlng)

        c = Court.objects.create(
            name=fake.company(),
            address=fake.address(),
            location=Point(float(latlng[1]), float(latlng[0])),
            types=random.choice([Court.CourtType.TENNIS, Court.CourtType.PICKLEBALL, Court.CourtType.BADMINTON]),
            buy_membership=fake.boolean(),
            num_courts=fake.random_int(0, 10),
            phone=fake.msisdn(),
            info=fake.text(),
            rating=fake.random_int(1, 5),
            website=fake.url(),
            verified=fake.boolean(),
            cost=random.choice([Court.PaidType.UNKNOWN, Court.PaidType.PAID, Court.PaidType.FREE]),
            need_membership=fake.boolean(),
            has_lighting=fake.boolean(),
        )
        c.images.set(random_photos)
        c.save()
        return c
