from django.shortcuts import render,HttpResponse,redirect
from detail.models import Employee_detail

# Create your views here.

def Table(request):
    show=Employee_detail.objects.all()
    data={'show':show}
    return render(request,'index.html',data)

def Create(request):
    if request.method=="POST":
        name=request.POST['name']
        sname=request.POST['lname']
        email=request.POST['email']
        phone =request.POST['phone']
        state=request.POST['state']
        city=request.POST['city']
        skills=request.POST['skill']
        experience=request.POST['experience']
        reference=request.POST['refer']
        file=request.POST['file']
        address=request.POST['address']
        
        d=Employee_detail(firstname=name,
                          secondname=sname,email=email,
                          phone=phone,state=state,city=city,skills=skills,experience=experience,reference=reference,
                          file=file,address=address)
        d.save()
        return redirect("cre1")
    
    return render (request,'create.html')
    