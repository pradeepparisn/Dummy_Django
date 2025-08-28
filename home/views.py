from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def developerinfo(request):
    return render(request,'developerinfo.html')