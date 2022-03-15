from django.urls import path
from .views import TeacherView,TeacherDetailView

urlpatterns = [
    path('',TeacherView.as_view(),name="teacher_list"),
    path('teacher/<int:pk>',TeacherDetailView.as_view(),name="teacher_detail"),








]
