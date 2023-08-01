from django.db import models
from django.contrib.auth.models import User, Group


class Module(models.Model):
    CATEGORY_CHOICES = [
        ("elective", "Elective"),
        ("compulsory", "Compulsory"),
    ]

    name = models.CharField(max_length=100)
    code = models.SlugField(max_length=10)
    credit = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    availability = models.BooleanField(default=True)
    courses_allowed = models.ManyToManyField(Group, related_name='modules')

    def __str__(self):
        return self.name
    

    @property
    def module_registrations(self):
        return [
            {"student": registration.student, "date": registration.date_of_registration}
            for registration in self.registrations.all()
        ]

class Student(models.Model):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="other")
    photo = models.ImageField(upload_to="student_photos/", default="default.jpg")
    course = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.first_name
    
    def registered_on_module(self, module):
        return self.student_registrations.filter(module=module).exists()


class Registration(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE, related_name="student_registrations")
    module = models.ForeignKey("Module", on_delete=models.CASCADE, related_name="registrations")
    date_of_registration = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'module')

    def __str__(self):
        return f"Registration #{self.id}: {self.student} - {self.module}"
