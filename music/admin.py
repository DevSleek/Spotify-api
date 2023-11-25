from django.contrib import admin
from .models import Artist, Album, Song


admin.site.register([Artist, Album, Song])