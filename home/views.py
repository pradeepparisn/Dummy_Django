from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact,Applicant
# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("this is home page")

def appliedcontact(request):
    contact=Contact.objects.all()
    return render(request,'appliedcontact.html',{'contact':contact})

def contact(request):
    if request.method== 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact=Contact(name=name,email= email ,phone= phone , desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')


def apply(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        paddress=request.POST.get('paddress')
        dob=request.POST.get('dob')
        branch=request.POST.get('branch')
        applicant=Applicant(name=name,email=email,paddress=paddress,dob=dob,branch=branch,date=datetime.today())
        applicant.save()   
    return render(request,'apply.html')