from django.urls import path, include
from . import views

app_name = "studentreg"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("course/<int:id>", views.course_detail, name="course_detail"),
    path("module/<str:code>", views.module_detail, name="module_detail"),
    path("module_register/<str:code>", views.module_register, name="module_register"),
    path(
        "module_unregister/<str:code>",
        views.module_unregister,
        name="module_unregister",
    ),
]
