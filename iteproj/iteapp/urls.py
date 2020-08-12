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
    path('services/airconditioning-system', views.services_airconditioning_system, name="services_airconditioning_system"),
    path('services/automatic-fire-supression-system', views.services_automatic_fire_supression_system, name="services_automatic_fire_supression_system"),
    path('services/fire-detection-and-alarm-system', views.services_fire_detection_and_alarm_system, name="services_fire_detection_and_alarm_system"),
    path('services/structured-cabling-for-network-and-telephone-system', views.services_structured_cabling_for_network_and_telephone_system, name="services_structured_cabling_for_network_and_telephone_system"),
    path('services/cctv-system', views.services_cctv_system, name="services_cctv_system"),
    path('services/food-safety-health-hygiene-quality-assurance', views.services_fshhqa, name="services_fshhqa"),
]