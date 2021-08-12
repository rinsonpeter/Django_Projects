from django.contrib import admin
from AppWorks.models import ModelWorkTypes, ModelProject, ModelWorkStatus, ModelWorks
# Register your models here.

admin.site.register(ModelWorks)
admin.site.register(ModelProject)
admin.site.register(ModelWorkStatus)
admin.site.register(ModelWorkTypes)

