from operator import truediv
from tokenize import blank_re
from django.db import models

# Create your models here.

# Cada clase va a representar una base de datos, y se va a declarar cada una de las columnas dentro con su tipo

class Project(models.Model): 
    title = models.CharField(max_length=100, verbose_name = 'Título')  # Warning no usar la constante MAX_LENGHT !
    description = models.TextField(verbose_name = 'Descripción')
    image = models.ImageField(verbose_name = 'imagen', upload_to = 'projects')
    link = models.URLField(verbose_name = 'Dirección Web', null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'fecha de creación') 
    updated = models.DateTimeField(auto_now = True, verbose_name = 'fecha de modificación')

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']
    
    def __str__(self):
        return self.title