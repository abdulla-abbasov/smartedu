from django.urls import path
from .views import Index,About,ContactView

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('about/',About.as_view(),name="about"),
    path('contact/',ContactView.as_view(),name="contact"),



]
