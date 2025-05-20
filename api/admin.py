from django.contrib import admin
from .models import *
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Member)


# class EventResource(resources.ModelResource):

#     class Meta:
#         model = Event


# @admin.register(Event)
# class EventAdmin(ImportExportModelAdmin):
#     list_display = ("title", "start")
#     pass
