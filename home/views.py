from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Feedback,Applicant
# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("this is home page")

#def appliedcontact(request):
 #   mail=None
  #  if request.method=='POST':
   #     mail=request.POST.get('mail')
    #    print(mail)
    #contact=Contact.objects.all()
    #return render(request,'appliedcontact.html',{'contact':contact,'mail':mail})

def feedback(request):
    con=None
    mail=None
    if request.method == 'POST':    
        if 'name' in request.POST and 'email' in request.POST and 'phone' in request.POST:
            name= request.POST.get('name')
            email= request.POST.get('email')
            phone= request.POST.get('phone')
            desc= request.POST.get('desc')
            feedback=Feedback(name=name,email= email ,phone= phone , desc=desc,date=datetime.today())
            feedback.save()
            

        elif 'mail' in request.POST:
            if request.method == 'POST':
                mail=request.POST.get('mail')
    feed=Feedback.objects.all()
    return render(request,'feedback.html',{'feed':feed,'mail':mail})


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