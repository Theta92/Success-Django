from django.contrib import admin

# Register your models here.
from .models import Student, Module, Registration


admin.site.register(Student)
admin.site.register(Module)
admin.site.register(Registration)
