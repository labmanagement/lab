from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from lab.forms import *
from django.contrib.auth import login
from lab.models import *
# Create your views here.
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import razorpay

from django.http import HttpResponse


def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        orderid=request.POST.get("provider_order_id")
        bookingid=request.POST.get("bookingid")
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": float(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Ordernow.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order['id'],    bookingid_id=bookingid
        )
        order.save()
        return render(
            request,
            "payment.html",
            {
                "callback_url": "http://127.0.0.1:8000/callback/",
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "order": order,
            },
        )
    return render(request, "payment.html")


@csrf_exempt
def callback(request):
    
    razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    #    return client.utility.verify_payment_signature(response_data)

    if request.method == "POST":
        try:
            payment_id = request.POST.get("razorpay_payment_id", "")
            provider_order_id = request.POST.get("razorpay_order_id", "")
            signature_id = request.POST.get("razorpay_signature", "")
            params_dict={
                'razorpay_order_id':provider_order_id,
                'razorpay_payment_id':payment_id,
                'razorpay_signature':signature_id

            }
            print(params_dict)
            try:
                order = Ordernow.objects.get(provider_order_id=provider_order_id)
            except:
                return HttpResponse("505 not found inner")
            order.payment_id = payment_id
            order.signature_id = signature_id
            order.save()
            
            result=razorpay_client.utility.verify_payment_signature(params_dict)
            
            if result==True:
                amount=int(order.amount)
                
                try:
                   
                    '''res=razorpay_client.payment.capture(payment_id,{
                        "amount" : amount,
                        "currency" : "INR"
                        })
                    print(res)'''
                    order.status=PaymentStatus.SUCCESS
                    order.save()
                    return render(request, "sucess.html")
                except:
                   
                    order.status=PaymentStatus.FAILURE
                    order.save()
                    return render(request, "failure.html")
            else:
                
                order.status=PaymentStatus.FAILURE
                order.save()
                return render(request, "failure.html")
        except:
            return HttpResponse("505 not found here")
        


class Homeview(TemplateView):
    template_name="Home.html"
class AboutUsview(TemplateView):
    template_name="About Us.html"
class Servicesview(TemplateView):
    template_name="Services.html"    

class contactview(TemplateView):
    template_name="contact.html"  
def insertcontact(request):
    if request.method=='POST':
        form=contectform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else: 
        form=contectform()
    return render(request,"contact.html",{'form':form}) 

def blogview(request):
    blg=blog.objects.all()
    return render(request,"blog.html",{'blg':blg})

def blogdetail(request,id):
    blg=blog.objects.get(id=id)
    return render(request,"blogdetail.html",{'blg':blg})

def FAQview(request):
    F=FAQ.objects.all()
    return render(request,"FAQ.html",{'F':F})

def Labview(request):
    lb=Lab.objects.all()
    return render(request,"Lab.html",{'lb':lb})


def signupview(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/blog/')
    else:
        form=signupform()
    return render(request,"registration/signup.html",{'form':form})

def testingview(request):
    t=Testing.objects.all()
    return render(request,"test.html",{'t':t})


def testdetail(request,id):
    t=Testing.objects.get(id=id)
    return render(request,"testdetail.html",{'t':t})
 
def Appointmentview(request):
    t=Testing.objects.all()
    l=Lab.objects.all()
    return render(request,"Appointment.html",{'t':t,'l':l})

        
def insertAppointment(request):
    if request.method=='POST':
        form=appointmentform(request.POST)
        if form.is_valid():
            obj=form.save()
            id=obj.pk
            return redirect('thankyou',id=id)
    else: 
        form=appointmentform()
    return render(request,"Appointment.html",{'form':form}) 

def thankyouview(request,id):
    i=Appointment.objects.get(id=id)
    return render(request,"thankyou.html",{'i':i})

def PatientReportsview(request):
    p=PatientReports.objects.filter(Userid_id=request.user.id)
    return render(request,"PatientReports.html",{'p':p})

def insertSubcribe(request):
    if request.method=='POST':
        form=Subcribeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Home/')
    else: 
        form=Subcribeform()
    return render(request,"Home.html",{'form':form}) 

def updatefeedbackview(request):
    id=request.POST.get("id")
    PatientFeedback=request.POST.get("PatientFeedback")
    obj=PatientReports.objects.get(id=id)
    obj.PatientFeedback=PatientFeedback
    obj.save()
    return redirect('/PatientReports')
