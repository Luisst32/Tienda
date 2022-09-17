from django.contrib import admin
from .models import productos 
from .models import Categorias


# Register your models here.
admin.site.register(productos)
admin.site.register(Categorias)