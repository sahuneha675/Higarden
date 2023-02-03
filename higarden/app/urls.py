from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="index"),
    path('about_us/',views.about, name="about"),
    path('contact_us/',views.contact, name="contact"),
    path('contact_us_data/',views.contact_us_data, name="contact_form"),



   
]
