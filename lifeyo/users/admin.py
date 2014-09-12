from django.contrib import admin
from .models import TestUser

class TestUserAdmin(admin.ModelAdmin):
    pass
    
    
admin.site.register(TestUser, TestUserAdmin)