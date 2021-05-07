from django.shortcuts import render, HttpResponse
from datetime import datetime
from Vivek.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    content = {
        "variable" : "Mrunu"
    }
    return render(request, 'Bat.html',content)
    # return HttpResponse("this is Vivek Homepaage")
    
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about Vivek")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is Viveks's services")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('name')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your contact has been sent!')
    return render(request, 'contact.html')
    # return HttpResponse("this is Viveks contact")