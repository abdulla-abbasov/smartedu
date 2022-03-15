from django.shortcuts import render
from.models import Course,Category,Tag
# Create your views here.
def course_list(request):
    categories=Category.objects.all()
    tags=Tag.objects.all()
    current_user=request.user
    if current_user.is_authenticated:
        enrolled_courses=Course.objects.filter(students=current_user)
        courses=Course.objects.all().order_by('-date')
        for course in enrolled_courses:
            courses=courses.exclude(id=course.id)
    else:
        courses=Course.objects.all()        
    return render(request,'courses.html',context={'courses':courses,'categories':categories,'tags':tags})

def course_detail(request,category_slug,course_id):
    course=Course.objects.get(category__slug=category_slug,id=course_id)  
    current_user=request.user
    courses=Course.objects.all().order_by('-date')
    categories=Category.objects.all()
    tags=Tag.objects.all()
    
    if current_user.is_authenticated:
        enrolled_courses=Course.objects.filter(students=current_user)
    else:
        enrolled_courses=course

 
    return render(request,'course.html',context={'course':course,'enrolled_courses':enrolled_courses,'categories':categories,'tags':tags}) 

def category_list(request,category_slug):
    categories=Category.objects.all()
    courses=Course.objects.filter(category__slug=category_slug)  
    return render(request,'courses.html',context={'courses':courses,'categories':categories})  


def tag_list(request,tag_slug):
    tags=Tag.objects.all()
    courses=Course.objects.filter(tags__slug=tag_slug)
    return render(request,'courses.html',context={'tags':tags,'courses':courses})


def search(request):
    courses=Course.objects.filter(name__contains=request.GET['search'])
    categories=Category.objects.all()
    tags=Tag.objects.all()
    return render(request,'courses.html',context={'courses':courses,'categories':categories,'tags':tags})
        