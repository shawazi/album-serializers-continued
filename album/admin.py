from django.contrib import admin
from .models import Song, Album, Artist, Genre
# Register your models here.

admin.site.register((Song, Album, Artist, Genre))
