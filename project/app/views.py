from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from pathlib import Path
from .models import Faculty,Student,Csbs,Csbs2,Csbs3,Sub
from django.template import loader
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64
val = None
def home(request):
    return render(request,"home.html")
def faculty(request):
    return render(request,"faculty.html")
def facultypage(request):
        #mydata =Sub.objects.filter(Staff=id).values() 
        #template = loader.get_template('facultypage.html')
        #context = {'m':mydata}
        #return HttpResponse(template.render(context, request))
        return render(request,"facultypage.html")
   
    
def student(request):
        return render(request,'student.html')
def signup(request):
        return render(request,'signup.html')

def facsignup(request):
        return render(request,'facsignup.html')
def stdsignup(request):
        return render(request,'stdsignup.html')
def Ssignup(request):
    if request.method=='POST':
        sname=request.POST['sname']
        reg=request.POST['reg']
        dept=request.POST['dept']
        clas=request.POST['class']
        spwd=request.POST['spwd']
        obj=Student()
        obj.Sname=sname
        obj.Reg=reg
        obj.Dept=dept
        obj.Class=clas
        obj.Psd=spwd
        obj.save()
        return render(request,"student.html")
def fsignup(request):
    if request.method=='POST':
        name=request.POST['name']
        id=request.POST['id']
        dept=request.POST['dept']
        phn=request.POST['phn']
        pwd=request.POST['pwd']
        obj=Faculty()
        obj.Name=name
        obj.Id=id
        obj.Dept=dept
        obj.Mobile=phn
        obj.Password=pwd
        obj.save() 
        return render(request,"faculty.html") 
def studentpage(request,reg):
        mydata =Student.objects.filter(Reg=reg).values() 
        template = loader.get_template('studentpage.html')
        context = {'m':mydata}
        return HttpResponse(template.render(context, request))
        #return render(request,"studentpage.html") 
        
def csbs(request):
        if request.method=='POST':
                reg=request.POST['reg']
                m1=request.POST['m1']
                m2=request.POST['m2']
                m3=request.POST['m3']
                m4=request.POST['m4']
                m5=request.POST['m5']
                obj=Csbs()
                obj.Reg=reg
                obj.Dm=m1
                obj.Oops=m2
                obj.Dbms=m3
                obj.Os=m4
                obj.Ds=m5
                obj.save() 
                return render(request,"facultypage.html")
def csbs2(request):
        if request.method=='POST':
                reg=request.POST['reg']
                m1=request.POST['m1']
                m2=request.POST['m2']
                m3=request.POST['m3']
                m4=request.POST['m4']
                m5=request.POST['m5']
                obj=Csbs2()
                obj.Reg=reg
                obj.Dm=m1
                obj.Oops=m2
                obj.Dbms=m3
                obj.Os=m4
                obj.Ds=m5
                obj.save() 
                return render(request,"ia2.html")

def csbs3(request):
        if request.method=='POST':
                reg=request.POST['reg']
                m1=request.POST['m1']
                m2=request.POST['m2']
                m3=request.POST['m3']
                m4=request.POST['m4']
                m5=request.POST['m5']
                obj=Csbs3()
                obj.Reg=reg
                obj.Dm=m1
                obj.Oops=m2
                obj.Dbms=m3
                obj.Os=m4
                obj.Ds=m5
                obj.save() 
                return render(request,"ia3.html")

def stdlogin(request):
    if request.method=='POST':
         reg=request.POST['reg']
         pwd=request.POST['pas']
         ob=Student.objects.filter(Reg=reg,Psd=pwd).values() 

         if ob : 
                template = loader.get_template('studentpage.html')
                context = {'m':ob}
                return HttpResponse(template.render(context, request))
         else:
                return render(request,'student.html') 
  


        
def cia1(request,reg):
        n= Csbs.objects.filter(Reg=reg).values()
        y=Student.objects.filter(Reg=reg).values()
        #z=Sub.objects.filter(Dep=y[0]['Dept'],year=y[0]['Class']).values()
       # print(z)
        if n:
                template = loader.get_template('cia1.html')
                context = {
                'y':y,
                'n': n,
                }
                return HttpResponse(template.render(context, request))
        else:
                 template = loader.get_template('cia1.html')
                 return HttpResponse(template.render({'y':'nodata'}, request))
def cia3(request,reg):
        n= Csbs3.objects.filter(Reg=reg).values()
        y=Student.objects.filter(Reg=reg).values()

        if n :

                template = loader.get_template('cia3.html')
                context = {
                'y':y,
                'n': n,
        
                }
                return HttpResponse(template.render(context, request))
        else:
                print("non data")
def cia2(request,reg):
        n= Csbs2.objects.filter(Reg=reg).values()
        y=Student.objects.filter(Reg=reg).values()

        if n:
                template = loader.get_template('cia2.html')
                context = {
                'y':y,
                'n': n,}
                return HttpResponse(template.render(context, request))
        else:
                print("non data")

def facultyfront(request):
        if request.method=='POST':
                reg=request.POST['Uid']
                pwd=request.POST['Pass']
                ob=Faculty.objects.filter(Id=reg,Password=pwd).values() 
        
                if ob : 
                        template = loader.get_template('facultyfront.html')
                        context = {'m':ob}
                        return HttpResponse(template.render(context, request))
                else:
                        return render(request,'faculty.html') 

   


    
def ia2(request):
        #mydata =Sub.objects.filter(Staff=id).values() 
        #template = loader.get_template('ia2.html')
        #context = {'m':mydata}
        #return HttpResponse(template.render(context, request))
        return render(request,'ia2.html')
def ia3(request):
        #mydata =Sub.objects.filter(Staff=id).values() 
        #template = loader.get_template('ia3.html')
        #context = {'m':mydata}
        #return HttpResponse(template.render(context, request))
        return render(request,'ia3.html')
def progress(request,reg):
        a= Csbs.objects.filter(Reg=reg).values()
        b= Csbs2.objects.filter(Reg=reg).values()
        c= Csbs3.objects.filter(Reg=reg).values()
        template = loader.get_template('progress.html')
        context = {
        'a':a,
        'b': b,
        'c':c
        }
      
      
       # print(type(a))
        import pandas as pd     
        import matplotlib.pyplot as plt
        plotdata = pd.DataFrame({

        "CIA1":[a[0]['Dm'],a[0]['Oops'],a[0]['Dbms'],a[0]['Os'],a[0]['Ds']],

        "CIA2":[b[0]['Dm'],b[0]['Oops'],b[0]['Dbms'],b[0]['Os'],b[0]['Ds']],

        "CIA3":[c[0]['Dm'],c[0]['Oops'],c[0]['Dbms'],c[0]['Os'],c[0]['Ds']],
        },

        index=["DM", "OOPS", "DBMS", "OS","DS"])

        plotdata.plot(kind="bar",figsize=(8,5))

        plt.title("Progress")

        plt.xlabel("Subjects")

        plt.ylabel("Marks")
       

        y = plt.gcf()
        buf = io.BytesIO()
        y.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri =  urllib.parse.quote(string)
        return render(request,'progress.html',{'y':uri,'a':a,'b':b,'c':c})
        #rr=HttpResponse(template.render(context, request))





