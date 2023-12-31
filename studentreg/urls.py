from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ModuleListView, StudentViewSet, RegistrationCreateView

router = DefaultRouter()
router.register(r'students', StudentViewSet)


app_name = "studentreg"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("course/", views.courses, name="courses"),
    path("course/<int:id>", views.course_detail, name="course_detail"),
    path("module/<str:code>", views.module_detail, name="module_detail"),
    path("module_register/<str:code>", views.module_register, name="module_register"),
    path(
        "module_unregister/<str:code>",
        views.module_unregister,
        name="module_unregister",
    ),
    path("my-registration/", views.my_registrations, name="my_registrations"),
    path("module/<str:code>/submit-feedback/", views.module_feedback, name="module_feedback"),
    path('api/modules/', ModuleListView.as_view(), name='module-list'),
    path('api/registrations/create/', RegistrationCreateView.as_view(), name='registration-create'),
    path('api/', include(router.urls)),

]
