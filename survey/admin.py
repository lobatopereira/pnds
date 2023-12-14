from django.contrib import admin
from .models import Survey
from import_export.admin import ImportExportModelAdmin
from import_export import resources
class SurveyResource(resources.ModelResource):
    class Meta:
        model = Survey
class SurveyAdmin(ImportExportModelAdmin):
    resource_class = SurveyResource
admin.site.register(Survey, SurveyAdmin)
# Register your models here.
