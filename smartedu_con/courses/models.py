from django.db import models
from teachers.models import Teacher

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,unique=True,null=True)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,unique=True,null=True)
    def __str__(self):
        return self.name        




class Course(models.Model):
    teacher=models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,unique=True,verbose_name="Kurs adi")
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    tags=models.ManyToManyField(Tag,null=True,blank=True)
    students=models.ManyToManyField(User,blank=True,related_name='joined_course')
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to="courses/%Y/%m/%d/",default="courses/default.jpg")
    date=models.DateTimeField(auto_now=True)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    