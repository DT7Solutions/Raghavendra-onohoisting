from django.contrib import admin
# from django.utils import timezone
from django.utils.html import format_html
import csv
from django.http import HttpResponse




# Register your models here.
from .models import RegisterUsers, Orders,User_info

class AdminRegister(admin.ModelAdmin):
    list_display=('UserID','FirstName','LastName','EmailID','Phone','Password')

class AdminProfile(admin.ModelAdmin):
    list_display=('phonenumber','firstname','lastname','email','city')

class AdminOrder(admin.ModelAdmin):
    list_display=('OrderID','Name','WhatsappNo','ContactNo','Date','Address','OrderStatus','file','TransactionId')
    list_filter= ['Name','WhatsappNo','Date','TransactionId','OrderStatus']
    search_fields = ['WhatsappNo','OrderStatus','Date']
    date_hierarchy = 'Date'
    actions = ['export_to_csv']
    def export_to_csv(self, request,queryset):
        meta = self.model._meta
        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=export.csv'
        writer = csv.writer(response)
        writer.writerow(fieldnames)
        for obj in queryset:
             writer.writerow([getattr(obj, field) for field in fieldnames])
        return response
    export_to_csv.short_description = "Download selected as csv"

    
admin.site.register(RegisterUsers,AdminRegister)
admin.site.register(Orders,AdminOrder)
admin.site.register(User_info,AdminProfile)


