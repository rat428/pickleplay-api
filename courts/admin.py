from django.contrib import admin
from .models import Court
# from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

# Register your models here.


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
