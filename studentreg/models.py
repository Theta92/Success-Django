from django.db import models
from django.contrib.auth.models import User, Group

# For creating modules and their attributes
class Module(models.Model):
    CATEGORY_CHOICES = [
        ("elective", "Elective"),
        ("compulsory", "Compulsory"),
    ]

    name = models.CharField(max_length=100)  # Name of the module
    code = models.SlugField(max_length=10)    # Code for identifying the module
    credit = models.IntegerField()            # Credit value of the module
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Category of the module
    description = models.TextField()          # Description of the module
    availability = models.BooleanField(default=True)  # Availability status
    courses_allowed = models.ManyToManyField(Group, related_name='modules')  # Courses allowed to take this module


    def __str__(self):
        return self.name

    @property
    def module_registrations(self):
        # Retrieve registrations for this module along with registration date
        return [
            {"student": registration.student, "date": registration.date_of_registration}
            for registration in self.registrations.all()
        ]

# Model For creating students and their attributes
class Student(models.Model):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # User associated with the student
    date_of_birth = models.DateField(null=True, blank=True)     # Date of birth of the student
    address = models.CharField(max_length=100, null=True, blank=True)  # Address of the student
    city = models.CharField(max_length=50, null=True, blank=True)      # City of residence
    country = models.CharField(max_length=50, null=True, blank=True)   # Country of residence
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="other")  # Gender of the student
    photo = models.ImageField(upload_to="student_photos/", default="default.jpg")  # Student's photo
    course = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)  # Course associated with the student


    def __str__(self):
        return self.user.first_name
    
    def registered_on_module(self, module):
    # Check if the student is registered on the given module
        return self.student_registrations.filter(module=module).exists()


# Model for managing module registrations
class Registration(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE, related_name="student_registrations")
    module = models.ForeignKey("Module", on_delete=models.CASCADE, related_name="registrations")
    date_of_registration = models.DateField(auto_now_add=True) # Date of registration

    class Meta:
        unique_together = ('student', 'module') # Ensure unique registrations for each student-module pair

    def __str__(self):
        return f"Registration #{self.id}: {self.student} - {self.module}"
