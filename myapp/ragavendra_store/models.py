from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
# Create your models here.

class RegisterUsers(models.Model):
    UserID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=20, blank=False)
    LastName = models.CharField(max_length=20, blank=False)
    EmailID = models.EmailField()
    Phone = models.IntegerField()
    Password = models.CharField(max_length=25, blank=False)
    Address =  models.CharField(max_length=255,null=True, blank=True)
    City =  models.CharField(max_length=25,null=True, blank=True)
    State =  models.CharField(max_length=25,null=True, blank=True)
    Zip = models.CharField(max_length=10,default=0,null=True, blank=True)
    UserStatus = models.BooleanField(default=True)

    def __int__(self):
            return self.UserID
    
class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    Name  = models.CharField(max_length=30,null=True, blank=True)
    WhatsappNo = models.BigIntegerField(null=True, blank=True)
    ContactNo = models.BigIntegerField(null=True, blank=True)
    Dono = models.CharField(max_length=250, blank=False,default="")
    LandMark = models.CharField(max_length=250, blank=False,default="")
    Area_name = models.CharField(max_length=255,null=True, blank=True,default="")
    Village = models.CharField(max_length=255,null=True, blank=True,default="")
    Mandal = models.CharField(max_length=255,null=True, blank=True,default="")
    District = models.CharField(max_length=255,null=True, blank=True,default="")
    State = models.CharField(max_length=255,null=True, blank=True,default="")
    Postal_code = models.CharField(max_length=10,null=True, blank=True,default="")
    Courier = models.CharField(max_length=30, blank=False)
    TransactionId = models.CharField(max_length=25,default=0,null=True, blank=True)
    TrackingId = models.CharField(max_length=10,default=0,null=True, blank=True)
    No_Of_Items = models.IntegerField(null=True, blank=True)
    item_color = models.CharField(max_length=10,null=True, blank=True)
    item_size = models.CharField(max_length=10,null=True, blank=True)
    
    file = models.FileField()
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Production', 'Production'),
        ('Out of Delivery', 'Out of Delivery'),
        ('completed', 'completed'),
    )
    OrderStatus = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    Date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   
   
    def __int__(self):
            return self.OrderID
    
class User_info(models.Model):
    phonenumber = models.BigIntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    Reciepentname = models.CharField(max_length=100,null=True, blank=True)
    Dono = models.CharField(max_length=250, blank=False,default="")
    LandMark = models.CharField(max_length=250, blank=False,default="")
    Area_name = models.CharField(max_length=255,null=True, blank=True,default="")
    Village = models.CharField(max_length=255,null=True, blank=True,default="")
    Mandal = models.CharField(max_length=255,null=True, blank=True,default="")
    District = models.CharField(max_length=255,null=True, blank=True,default="")
    State = models.CharField(max_length=255,null=True, blank=True,default="")
    Postal_code = models.CharField(max_length=10,null=True, blank=True,default="")
    # city = models.CharField(max_length=100,null=True, blank=True)
    # state = models.CharField(max_length=100,null=True, blank=True)
    # zip_code = models.CharField(max_length=10,null=True, blank=True)
    # address = models.TextField(null=True, blank=True)
    Address_type = models.CharField(max_length=25,null=True, blank=True)
    userid = models.IntegerField(null=True, default=0)

    def __int__(self):
        return self.Reciepentname
    



# class User_info(models.Model):
#     phonenumber = models.IntegerField()
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     email = models.EmailField()
#     userid = models.IntegerField(null=True, default=0)
    

#     def __str__(self):
#         return self.firstname

# class Address(models.Model):
#     ADDRESS_TYPES = (
#         ('home', 'Home'),
#         ('personal', 'Personal'),
#         ('work', 'Work'),
#     )

#     user_info = models.ForeignKey(User_info, on_delete=models.CASCADE, related_name='addresses')
#     address_type = models.CharField(max_length=10, choices=ADDRESS_TYPES)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=10)
#     address = models.TextField()

#     def __str__(self):
#         return f"{self.address_type} Address for {self.user_info.firstname} {self.user_info.lastname}"

