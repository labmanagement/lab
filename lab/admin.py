from django.contrib import admin
from lab.models import*
# Register your models here.

@admin.register(contect)
class contactadmin(admin.ModelAdmin):
    list_display=('firstname','email','subject','message')

@admin.register(product)
class productadmin(admin.ModelAdmin):
    pass

@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    pass

@admin.register(FAQ)
class FAQadmin(admin.ModelAdmin):
    pass

@admin.register(Lab)
class Labadmin(admin.ModelAdmin):
    pass

@admin.register(Testing)
class Testingadmin(admin.ModelAdmin):
    pass

@admin.register(Appointment)
class Appointmentadmin(admin.ModelAdmin):
    list_display=('Name','DOB','Gender','PhoneNo','Appointmentdate','Appointmenttime','Labid','Testid','Bookingdate')

@admin.register(PatientReports)
class PatientReportsadmin(admin.ModelAdmin):
    pass

@admin.register(Subcribe)
class Subcribeadmin(admin.ModelAdmin):
    pass
