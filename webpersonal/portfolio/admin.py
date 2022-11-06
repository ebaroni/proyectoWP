from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin) # Registro la app para poder verla en el admin. En el admin me agrega la clase/base de datos en plural: Projects. Es una convencion que sea así.
