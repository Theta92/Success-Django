from django.urls import path
from . import views

app_name = "studentreg"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("modules/", views.modules, name="modules"),
]
