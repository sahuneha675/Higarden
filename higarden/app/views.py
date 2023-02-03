from django.shortcuts import redirect,render
from .models import *

# Create your views here.
def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def contact_us_data(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['message']
        
        Person.objects.create(name=name,email=email,subject=subject,msg=msg)
        return redirect('/contact_us/')

        