from django.db import models
from django.contrib.auth.models import User, Group

class Module(models.Model):
    CATEGORY_CHOICES = [
        ('elective', 'Elective'),
        ('compulsory', 'Compulsory'),
    ]

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    credit = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    availability = models.BooleanField(default=True)
    courses_allowed = models.ManyToManyField(Group)

    def __str__(self):
        return self.name



class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="student_photos/")

    def __str__(self):
        return self.address


class Registration(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    module = models.ForeignKey("Module", on_delete=models.CASCADE)
    date_of_registration = models.DateField()

    def __str__(self):
        return f"Registration #{self.id}: {self.student} - {self.module}"
