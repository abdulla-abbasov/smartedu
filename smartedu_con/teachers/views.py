from django.shortcuts import render
from .models import Teacher
from courses.models import Course
from django.views import generic
# Create your views here.


class TeacherView(generic.ListView):
    model=Teacher
    template_name='teachers.html'
    context_object_name='teachers'


class TeacherDetailView(generic.DetailView): 
    model=Teacher  
    template_name='teacher.html'
    context_object_name='teacher'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True,teacher=self.kwargs['pk'])
        return context
