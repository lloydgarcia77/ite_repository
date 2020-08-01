from django.urls import path
from iteapp import views

app_name = "business-side"
urlpatterns = [
    path('about-us/', views.about_us, name="about_us"),
    path('projects/', views.projects, name="projects"),
    path('blogs/', views.blogs, name="blogs"),
    path('testimony/', views.testimony, name="testimony"),
    path('contact/', views.contact, name="contact"),
    path('services/electrical-system', views.services_electrical_system, name="services_electrical_system"),
    path('services/solar-power-system', views.services_solar_power_system, name="services_solar_power_system"),
]