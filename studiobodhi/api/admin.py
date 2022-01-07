from django.contrib import admin
from .models import blogMOdel, urlModel, contactModel
# Register your models here.

admin.site.register(blogMOdel)
admin.site.register(contactModel)
admin.site.register(urlModel)