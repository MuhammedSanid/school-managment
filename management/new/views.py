from django.shortcuts import render,redirect
from new.models import User,Student,Teacher
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request): 
    return render(request,'main.html')

def logins(request): 
    if request.method =='POST':
        usr = request.POST['username']
        pas = request.POST['password']
        x = authenticate(request,username=usr,password=pas)
        if x is not None and x.approve_student=="approved":
            login(request,x)
            request.session['sid'] = x.id
            return render(request,'sthome.html',{"data":x})
        elif x is not None and x.usertype == 'teacher':
            login(request,x)
            request.session['tid'] = x.id
            return render(request,'tchome.html',{"data":x})
        elif x is not None and x.is_staff== 1:
            login(request,x)
            request.session['aid'] = x.id
            return render(request,'adhome.html')
        else:
            return redirect(logins)
    
    else:  
        return render(request,'login.html')

def Student_registration(request): 
    if request.method=='POST':
        na = request.POST['name']
        em = request.POST['email']
        usr = request.POST['username']
        pas = request.POST['password']
        ph = request.POST['phone']
        db = request.POST['dob']
        ss=User.objects.create_user(first_name=na,email=em,username=usr,password=pas,usertype="student",approve_student="waiting")
        s=Student.objects.create(name=na,email=em,phone=ph,dob=db,stud=ss)
        s.save()
        return redirect(logins)
    else:
        
        return render(request,'stregistration.html')

def Teacher_registration(request): 
     if request.method=='POST':
        na = request.POST['name']
        em = request.POST['email']
        usr = request.POST['username']
        pas = request.POST['password']
        ph = request.POST['phone']
        dp = request.POST['dep']
        ts=User.objects.create_user(first_name=na,email=em,username=usr,password=pas,usertype="teacher")
        T=Teacher.objects.create(name=na,email=em,phone=ph,dep=dp,tch=ts) 
        T.save()
        return redirect(logins)
     else:
       return render(request,'tcregistration.html')
   
def logouts(request):
    logout(request)
    return redirect(index)

# student functions
def vw_st(request):
    str=Student.objects.all()
    return render(request,"view_std.html",{"data":str})
def st_home(request):
    str=Student.objects.all()
    return render(request,"sthome.html",{"data":str})

def view_student(request):
    st= Student.objects.all()
    return render(request,'view_student.html',{'data':st})

def edit_student(request,id):
    st=Student.objects.get(id=id)
    q= User.objects.get(id=st.stud_id)
    return render(request,"edit_student.html",{"data":st,"val":q})
        
def upd_student(request,id,idd):
    if request.method=='POST':
        na=request.POST.get("name")
        em=request.POST.get("email")
        ph=request.POST.get("phone")
        db=request.POST.get("dob")
        new_stt=User.objects.filter(id=idd).update(first_name=na,email=em)
        new_st=Student.objects.filter(id=id).update(name=na,email=em,phone=ph,dob=db)
        return redirect(view_student)
    else:
        return redirect(edit_student)
def delete_student(request,id):
    std= User.objects.get(id=id)
    std.delete()
    return redirect(view_student)


# teacher functions 
def vw_tcr(request):
    ts= Teacher.objects.all()
    return render(request,'view_tcr.html',{'data':ts})
def tc_home(request):
    str=Teacher.objects.all()
    return render(request,"tchome.html",{"data":str}) 

def view_teacher(request):
    ts= Teacher.objects.all()
    return render(request,'view_teacher.html',{'data':ts})
    
def edit_teacher(request,id):
    st=Teacher.objects.get(id=id)
    x = User.objects.get(id=st.tch_id)
    return render(request,"edit_teacher.html",{"data":st,"val":x})
        
def upd_teacher(request,id,idd):
    if request.method=='POST':
        na=request.POST.get("name")
        em=request.POST.get("email")
        ph=request.POST.get("phone")
        dp=request.POST.get("dep")
        new_ttr=User.objects.filter(id=idd).update(first_name=na,email=em)
        new_tr=Teacher.objects.filter(id=id).update(name=na,email=em,phone=ph,dep=dp)
        return redirect(view_teacher)
    else:
        return redirect(edit_teacher)
    
    
def delete_teacher(request,id):
    tc = User.objects.get(id=id)
    tc.delete()
    return redirect(view_teacher)



def approve(request):
    ap=User.objects.filter(approve_student="waiting")
    return render(request,"approve.html",{"data":ap})

def aprvd(request,id):
    User.objects.filter(id=id).update(approve_student="approved")
    return redirect(approve)

def edit_stud(request,id):
    r=request.session['sid']
    ed=User.objects.get(id=r)
    edt=Student.objects.get(stud_id=id)
    return render(request,"edit_stud.html",{"dataa":edt,"vala":ed})

def update_stud(request,id,idd):
    if request.method=='POST':
        na=request.POST.get("name")
        em=request.POST.get("email")
        ph=request.POST.get("phone")
        db=request.POST.get("dob")
        us=request.POST ["user"]
        ps=request.POST["password"]
        new_stt=User.objects.filter(id=idd).update(first_name=na,email=em,username=us,password=ps,user_type="student",approve_student="approved")
        new_st=Student.objects.filter(id=id).update(name=na,email=em,phone=ph,dob=db)
        return redirect(st_home)
    else:
        return redirect(edit_stud)


def edit_tcr(request,id):
    r=request.session['tid']
    ed=User.objects.get(id=r)
    edt=Teacher.objects.get(tch_id=id)
    
    return render(request,"edit_tcr.html",{"dataa":edt,"vala":ed})

def update_tcr(request,id,idd):
    if request.method=='POST':
        na=request.POST.get("name")
        em=request.POST.get("email")
        ph=request.POST.get("phone")
        dp=request.POST.get("dep")
        us=request.POST ["user"]
        ps=request.POST["password"]
        new_stt=User.objects.filter(id=idd).update(first_name=na,email=em,username=us,password=ps,user_type="teacher")
        new_st=Teacher.objects.filter(id=id).update(name=na,email=em,phone=ph,dep=dp)
        return redirect(logins)
    else:
        return redirect(edit_stud)
