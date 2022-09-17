
from ast import Str
from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from autoslug import AutoSlugField



# Create your models here

class Categorias(models.Model):
    nombre=models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='nombre')
    activo=models.BooleanField(default=True)
    def __str__(self)->Str:
        return self.nombre
        
    class Meta:
        verbose_name_plural='Categorias'


class productos(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='nombre')
    imagen=models.ImageField(upload_to='images')
    descripcion=models.TextField(blank=True,null=True)
    precio=models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    categoria=models.ForeignKey(Categorias, on_delete=models.CASCADE)
    destacado=models.BooleanField(default=True)
    actico=models.BooleanField(default=True)
    def __str__(self)->str:
        return self.nombre
        
    class Meta:
        verbose_name_plural='productos'






      
      