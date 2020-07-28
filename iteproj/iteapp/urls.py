from django.urls import path
from iteapp import views

app_name = "business-side"
urlpatterns = [
    path('about-us/', views.about_us, name="about_us"),
    path('projects/', views.projects, name="projects"),
    path('blogs/', views.blogs, name="blogs"),
    path('testimony/', views.testimony, name="testimony"),
    path('contact/', views.contact, name="contact"),
]