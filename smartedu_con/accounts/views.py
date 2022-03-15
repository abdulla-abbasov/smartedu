from django.shortcuts import render,redirect
from.forms import Loginform,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from courses.models import Course
from django.contrib.auth.models import User

# Create your views here.
def loginuser(request):
    form=Loginform()
    if request.method=='POST':
        form=Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username'] 
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
                
            
            else:
                messages.info(request,'bu adda istifadeci  movcud deyil')    
                return redirect('register')
    else:
        form=Loginform()
        return render(request,'login.html',context={'form':form})        
				
               

def registeruser(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'qeydiyat ugurla tamamlandi:)')
            return redirect('login')
    else:
        return render(request,'register.html',context={'form':form})        

        # return render(request,'register.html',context={'form':form})    


def logoutuser(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def dashboard(request):
    current_user=request.user
    courses=Course.objects.filter(students=current_user)
    return render(request,'dashboard.html',context={'courses':courses,'current_user':current_user })
  

def course_enroll(request):
    course_id=request.POST['course_id']
    user_id=request.POST['user_id'] 
    course=Course.objects.get(id=course_id)
    user=User.objects.get(id=user_id)
    course.students.add(user)
    return redirect('dashboard')


def course_release(request):
    course_id=request.POST['course_id']
    user_id=request.POST['user_id'] 
    course=Course.objects.get(id=course_id)
    user=User.objects.get(id=user_id)
    course.students.remove(user)
    return redirect('dashboard')    