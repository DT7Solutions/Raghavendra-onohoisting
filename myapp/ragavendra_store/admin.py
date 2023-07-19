from django.contrib import admin
# from django.utils import timezone
from django.utils.html import format_html
import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib import colors


# Register your models here.
from .models import RegisterUsers, Orders,User_info

class AdminRegister(admin.ModelAdmin):
    list_display=('UserID','FirstName','LastName','EmailID','Phone','Password')

class AdminProfile(admin.ModelAdmin):
    list_display=('phonenumber','firstname','lastname','email','city')


def generate_invoice_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    p = canvas.Canvas(response, pagesize=A4)

    # Define header and footer
    header_text = "Invoice"
    footer_text = "Your Company Footer"

    # Retrieve data from the order table
    orders = queryset.values('OrderID', 'Name', 'WhatsappNo', 'ContactNo', 'Date', 'Address')

    # Set logo and header
    logo_path = "static_files/images/raghavendra-textiles-admin-logo.png"  # Provide the path to your logo file
    p.drawImage(logo_path, 460, 610, width=80, height=80)  # Adjust the coordinates and dimensions as per your preference
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, 780, header_text)

    # Generate invoice PDF
    for order in orders:
        order_id = order['OrderID']
        customer_name = order['Name']
        whatsapp_no = order['WhatsappNo']
        contact_no = order['ContactNo']
        order_date = datetime.now()
        address = order['Address']

        # Render invoice details on the PDF canvas
        formatted_date = datetime.strftime(order_date, "%Y-%m-%d")
        p.setFont("Helvetica", 12)
        p.drawString(70, 700, f"S.No:________________")
        p.drawString(460, 700,f"Date: {formatted_date}")
        p.drawString(70, 680, f"Order ID: {order_id}")
        p.drawString(70, 660, f"Customer: {customer_name}")
        p.drawString(70, 640, f"WhatsApp No: {whatsapp_no}")
        p.drawString(70, 620, f"Contact No: {contact_no}")
        p.drawString(70, 600, f"Address: {address}")

        # Additional rendering logic for other invoice details

        p.showPage()  # Move to the next page for the next order

    # Set footer
    p.setFont("Helvetica", 10)
    p.setFillColor(colors.grey)
    p.drawString(50, 50, footer_text)

    p.save()
    return response

# def generate_invoice_pdf(modeladmin, request, queryset):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

#     p = canvas.Canvas(response)

#     # Retrieve data from the order table
#     orders = queryset.values('OrderID','Name','WhatsappNo','ContactNo','Date','Address')

#     # Generate invoice PDF
#     for order in orders:
#         order_id = order['OrderID']
#         customer_name = order['Name']
#         whatesappno = order['WhatsappNo']
#         contactno = order['ContactNo']
#         order_date = order['Date']
#         Address = order['Address']
#         formatted_date = datetime.strftime(order_date, "%Y-%m-%d")
#         # Render invoice details on the PDF canvas
#         p.drawString(100, 700, f"Order ID: {order_id}")
#         p.drawString(400, 700, f"Date: {formatted_date}")
#         p.drawString(100, 680, f"Customer: {customer_name}")
#         p.drawString(100, 660, f"WhatesAppNo: {whatesappno}")
#         p.drawString(100, 640, f"ContactNo: {contactno}")
#         # p.drawString(110, 700, f"Date: {formatted_date}")
#         p.drawString(100, 620, f"Address: {Address}")


#         # Additional rendering logic for other invoice details

#         p.showPage()  # Move to the next page for the next order

#     p.save()
#     return response

generate_invoice_pdf.short_description = "Generate Invoice PDF"
class AdminOrder(admin.ModelAdmin):
    list_display=('OrderID','Name','WhatsappNo','ContactNo','Date','Address','OrderStatus','file','TransactionId')
    list_filter= ['Name','WhatsappNo','Date','TransactionId','OrderStatus']
    search_fields = ['WhatsappNo','OrderStatus','Date']
    date_hierarchy = 'Date'
    actions = ['export_to_csv',generate_invoice_pdf]
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


