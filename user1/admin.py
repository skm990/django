from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User_profile,Teams,Team_members





admin.site.register(User_profile)
admin.site.register(Teams)
admin.site.register(Team_members)

# Register your models here.
