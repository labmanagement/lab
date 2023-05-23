from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
import datetime
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus

# Create your models here.
class contect(models.Model):
    firstname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    class meta:
        db_table="contect"

class product(models.Model):
    name=models.CharField(max_length=100)
    mrp=models.FloatField()
    Sellingprice=models.FloatField()
    description=models.TextField()
    photo=models.ImageField(upload_to='product/')
    class Meta:
        db_table="product"
    def __str__(self):
        return self.name
class blog(models.Model):
    title=models.CharField(max_length=200)
    description=HTMLField()
    photo=models.ImageField(upload_to='blog/')
    postby=models.CharField(max_length=50,default="Admin")
    poston=models.DateField(default=datetime.date.today())
    class Meta:
        db_table="blog"
    def __str__(self):
        return self.title   
    

class FAQ(models.Model):
    question=models.TextField()
    answer=models.TextField()
    class Meta:
        db_table="FAQ"
    def __str__(self):
        return self.question  
    

class Lab(models.Model):
     name=models.CharField(max_length=100)
     Address=models.CharField(max_length=100,default="")
     Location=models.TextField(default="")
     photo=models.ImageField(upload_to='lab/',default="") 
     class Meta:
         db_table="Lab"
     def __str__(self):
         return self.name
     

class Testing(models.Model):
    name=models.CharField(max_length=200)
    PackageIncludes=models.TextField(default="")
    description=HTMLField(default="")
    sampleType=models.CharField(max_length=100,default="")
    FastingRequirement=models.CharField(max_length=100,default="")
    TubeType=models.CharField(max_length=100,default="")  
    Reports=models.CharField(max_length=100,default="")   
    price=models.IntegerField(max_length=100)
    photo=models.ImageField(upload_to='Testing/',default="") 
    class Meta:
        db_table="Testing"
    def __str__(self):
        return self.name   
    
class Appointment(models.Model):
    Name=models.CharField(max_length=100)
    DOB=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20,default="")
    PhoneNo=models.CharField(max_length=20)
    Appointmentdate=models.CharField(max_length=20)
    Appointmenttime=models.CharField(max_length=20)
    Labid=models.ForeignKey(Lab,on_delete=models.CASCADE,blank=True,null=True)
    Testid=models.ForeignKey(Testing,on_delete=models.CASCADE,blank=True,null=True)
    Bookingdate=models.CharField(max_length=20)
    class Meta:
        db_table="Appointment"
    def __str__(self):
        return self.Name   


class PatientReports(models.Model):
    Userid=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    Reports=models.FileField(upload_to='PatientReports/')
    DoctorFeedback=models.TextField(default="")
    PatientFeedback=models.TextField(default="",null=True,blank=True)
    Report_date=models.DateField(auto_now=True)
    class Meta:
        db_table="PatientReports"
    def __str__(self):
        return self.DoctorFeedback 

class Subcribe(models.Model):
    Name=models.CharField(max_length=100)
    emailid=models.CharField(max_length=100,default="")
    class Meta:
        db_table="Subcribe"
    def __str__(self):
        return self.Name         





class Ordernow(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )
    bookingid=models.ForeignKey(Appointment,on_delete=models.CASCADE,blank=True,null=True,related_name="bookings")

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"

