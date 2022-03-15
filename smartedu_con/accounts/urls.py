from django.urls import path
from .views import loginuser,registeruser,dashboard,logoutuser,course_enroll,course_release

urlpatterns = [
    path('login/',loginuser,name="login"),
    path('logout/',logoutuser,name="logout"),

    path('register/',registeruser,name="register"),
    path('dashboard/',dashboard,name="dashboard"),
    path('course_enroll/',course_enroll,name="course_enroll"),
    path('course_release/',course_release,name="course_release")
]
