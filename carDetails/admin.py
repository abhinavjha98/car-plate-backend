from django.contrib import admin
from carDetails.models import CarDetails, PCNCode, PCNTable
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class CarDetailsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('number_plate','car_model','car_color','car_location','car_image',)
    search_fields = ('number_plate', )
    list_filter = ('car_model',)

class PCNAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('pcnCode',)
    search_fields = ('pcnCode', )
    list_filter = ('pcnCode',)

class PCNTableAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('user','carDetails','pcnCode','date_of_creation','reason')
    search_fields = ('user','pcnCode',)
    list_filter = ('user','pcnCode',)

admin.site.register(CarDetails,CarDetailsAdmin)
admin.site.register(PCNCode,PCNAdmin)
admin.site.register(PCNTable,PCNTableAdmin)
