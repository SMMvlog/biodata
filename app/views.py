from django.shortcuts import render,redirect
from .models import Resume
from .forms import ResumeForm
from django.views import View

# Create your views here.

class Home(View):
    def get(self,request):
        fm = ResumeForm()
        candidates = Resume.objects.all()
        return render(request,'home.html',{'fm':fm,'candidates':candidates})

    def post(self,request):
        fm = ResumeForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("/")
            
        else:
            candidates = Resume.objects.all()
            return render(request,'home.html',{'fm':fm,'candidates':candidates})
        
   
class candidate(View):
    def get(self,request,id):
        candidate = Resume.objects.get(id=id)
        return render(request,'candidate.html',{'candidate':candidate})

def DeleteCandedate(request,id):
    candidate = Resume.objects.get(id=id)
    candidate.delete()
    return redirect("/")

def UpdateCandedate(request,id):
    if request.method == "POST":
        candidate = Resume.objects.get(id=id)
        upt = ResumeForm(request.POST, request.FILES,instance=candidate)
        if upt.is_valid:
           upt.save()
           return redirect("/")
    candidate = Resume.objects.get(id=id)
    fm = ResumeForm(instance=candidate)
    return render(request,'update.html',{'candidate':candidate,'fm':fm})