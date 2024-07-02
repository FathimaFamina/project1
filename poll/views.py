from django.shortcuts import render
from django.http import HttpResponse,request,HttpResponseRedirect
from poll.forms import NameForm

from django.template import loader
from poll.models import Person
from django.views.decorators.csrf import csrf_exempt# Create your views here.
from django.db.models import Q
from django.core.files.storage import FileSystemStorage



def persons(request):
    template=loader.get_template('persons.html')
    per=Person.objects.all().values()
    context={
        'persons':per
    }
    return HttpResponse(template.render(context,request))

def perdetails(request,id):
    template=loader.get_template('perdetails.html')
    per=Person.objects.get(id=id)
    context={
        'person':per
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template=loader.get_template('main.html')
   
    return HttpResponse(template.render())

def addperson(request):
    template=loader.get_template('addperson.html')
   
    return HttpResponse(template.render())



@csrf_exempt

def addpersoncreate(request):
    if request.method=='POST' and request.FILES['imgupload']:
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        mob=request.POST['mob']
        dob=request.POST['dob']
        city=request.POST['city']
        state=request.POST['state']
        pin=request.POST['pin']
        upload = request.FILES['imgupload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        img = fss.url(file)



    print(fname,lname,email,mob,dob,city,state,pin,img)
    person=Person(fname=fname,lname=lname,email=email,mob=mob,dob=dob,city=city,state=state,pin=pin,img=img)
    person.save()
        
    template=loader.get_template('addsuccess.html')
   
    return HttpResponse(template.render())

def deleteperson(request,id):
    template=loader.get_template('deletesuccess.html')
    per=Person.objects.get(id=id)
    per.delete()
   
    return HttpResponse(template.render())




def update(request,id):
    template=loader.get_template('updateperson.html')
    person=Person.objects.get(id=id)
    context={
        'person':person
    }

   
    return HttpResponse(template.render(context,request))




@csrf_exempt

def updateperson(request,id):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
      
        dob=request.POST['dob']
        city=request.POST['city']
        state=request.POST['state']
        pin=request.POST['pin']


    person=Person.objects.get(id=id)
    person.fname=fname
    person.lname=lname
    person.dob=dob
    person.city=city
    person.city=state
    person.pin=pin
    
    person.save()
    context={
        'person':person
    }
        
    template=loader.get_template('updatesuccess.html')
   
    return HttpResponse(template.render(context,request))

def test(request):
    template=loader.get_template('test.html')
    person=Person.objects.all()
    context={
        'person':person,
     
      
    }

   
    return HttpResponse(template.render(context,request))

def ffn(request):
    template=loader.get_template('test.html')
    person=Person.objects.filter(fname='John')
    context={
        'person':person,
     
      
    }

   
    return HttpResponse(template.render(context,request))
def fln(request):
    template=loader.get_template('test.html')
    person=Person.objects.filter(lname='Doe')
    context={
        'person':person,
     
      
    }

   
    return HttpResponse(template.render(context,request))

def fc(request):
    template=loader.get_template('test.html')
    person=Person.objects.order_by('fname','id')
    context={
        'person':person,
     
      
    }

    

   
    return HttpResponse(template.render(context,request))