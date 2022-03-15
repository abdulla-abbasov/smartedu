
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from courses.models import Course
from.forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from teachers.models import Teacher

# Create your views here.
# def index(request):
#     return render(request,'index.html')

class Index(generic.TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True).order_by('-date')[:2]
        context['total_course']=Course.objects.filter(available=True).count()
        context['students']=User.objects.all().count()
        context['teachers']=Teacher.objects.all().count()


        return context

# def about(request):
#     return render(request,'about.html')    
class About(generic.TemplateView):
    template_name='about.html'
    
class ContactView(generic.FormView,SuccessMessageMixin):
    form_class=ContactForm
    template_name='contact.html' 
    success_url=reverse_lazy('contact')
    success_messages='Sizin mesajiniz qeyde alindi '

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
