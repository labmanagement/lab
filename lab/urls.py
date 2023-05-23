from django.urls import path, include
from lab import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
   
    path('Home/',views.Homeview.as_view() ),
    path('contact/',views.contactview.as_view() ),
    path('insertcontact/',views.insertcontact),
    path('blog/',views.blogview),
    path('blogdetail/<int:id>',views.blogdetail),
    path('FAQ/',views.FAQview),
    path('Labs/',views.Labview),
    #path('testing/',views.testingview),
    path('signup/',views.signupview),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('test/',views.testingview),
    path('testdetail/<int:id>',views.testdetail),
    path('About Us/',views.AboutUsview.as_view() ),
    path('Services/',views.Servicesview.as_view()),
    path('Appointment/',views.Appointmentview),
    path('insertAppointment/',views.insertAppointment),
    path('thankyou/<int:id>',views.thankyouview,name="thankyou"),
    path('PatientReports/',views.PatientReportsview),
    path('insertSubcribe/',views.insertSubcribe),
    path('updatefeedback/',views.updatefeedbackview),
    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
]

