from django.contrib import admin
from .models import Datavisualization
from import_export.admin import ImportMixin
from import_export import resources






class MyModelResource(resources.ModelResource):
    def get_instance(self):
        return False

    class Meta:
        model = Datavisualization
        fields = ['end_year','intensity','topic',]
        export_order = fields

class MyModelAdmin(ImportMixin, admin.ModelAdmin):
    instance = MyModelResource()






admin.site.register(Datavisualization,MyModelAdmin)

# Register your models here.
