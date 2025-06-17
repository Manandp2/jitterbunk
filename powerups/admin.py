from django.contrib import admin

# Register your models here.

from .models import Powerup, User

admin.site.register(Powerup)
admin.site.register(User)