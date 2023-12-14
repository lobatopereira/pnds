from django.contrib import admin
from .models import Programa,Implementasaun,ImplementasaunPoint
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class ProgramaResource(resources.ModelResource):
    class Meta:
        model = Programa
class ProgramaAdmin(ImportExportModelAdmin):
    resource_class = ProgramaResource
admin.site.register(Programa, ProgramaAdmin)


class ImplementasaunResource(resources.ModelResource):
    class Meta:
        model = Implementasaun
class ImplementasaunAdmin(ImportExportModelAdmin):
    resource_class = ImplementasaunResource
admin.site.register(Implementasaun, ImplementasaunAdmin)

class ImplementasaunPointResource(resources.ModelResource):
    class Meta:
        model = ImplementasaunPoint
class ImplementasaunPointAdmin(ImportExportModelAdmin):
    resource_class = ImplementasaunPointResource
admin.site.register(ImplementasaunPoint, ImplementasaunPointAdmin)
