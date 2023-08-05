from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
<<<<<<< HEAD
=======

>>>>>>> 21486e6 (Registration Page)

# Importing all forms
from .forms import (
    RegisterForm,
    UserUpdateForm,
    StudentProfileUpdateForm,
    StudentCreationForm,
)

# Password reset
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .models import Student, Module, Group, Registration


def home(request):
        # To retrieve all courses
    courses = Group.objects.all()
    context = {"title": "Welcome", "courses": courses}
    return render(request, "studentreg/home.html", context)


def about(request):
    return render(request, "studentreg/about.html", {"title": "About"})


def contact(request):
    return render(request, "studentreg/contact.html", {"title": "Contact"})

def courses(request):
    courses = Group.objects.all()
    return render(request, "studentreg/courses.html", {"title": "Courses","courses": courses })

# Register authentication
def register(request):
   # Initialize forms

    student_form = StudentCreationForm()
    register_form = RegisterForm()

    if request.method == "POST":
       # Get data from forms
        register_form = RegisterForm(request.POST)
        student_form = StudentCreationForm(request.POST)

        if register_form.is_valid() and student_form.is_valid():
         # To Create user and student objects
            user = register_form.save(commit=False)
            course = student_form.cleaned_data.get("course")
            gender = student_form.cleaned_data.get("gender")
            student = Student(user=user, course=course, gender=gender)
            user.save()
            student.save()
            messages.success(
                request, f"Your account has been created! Now you can login!"
            )
            return redirect("login")
        else:
            messages.warning(request, f"Unable to create account!") 

    context = {
        "title": "Register",
        "student_form": student_form,
        "register_form": register_form,
    }
    return render(request, "studentreg/register.html", context)

# To update profile (user has to be logged in)
@login_required
def profile(request):
    if request.method == "POST":
        # Get form data and update user and student profiles
        u_form = UserUpdateForm(request.POST, instance=request.user)
        sp_form = StudentProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.student
        )
        if u_form.is_valid and sp_form.is_valid:
            u_form.save()
            sp_form.save()
            messages.success(request, "Your account has been successfully updated")
            return redirect("profile")
    else:
        # Forms with existing user and student data
        u_form = UserUpdateForm(instance=request.user)
        sp_form = StudentProfileUpdateForm(instance=request.user.student)
    context = {"u_form": u_form, "sp_form": sp_form, "title": "Student Profile"}
    return render(request, "studentreg/profile.html", context)


def course_detail(request, id):
    # Get course details and modules associated with a course
    course = get_object_or_404(Group, id=id)
    context = {"title": "Modules", "course": course, "modules": course.modules.all()}
    return render(request, "studentreg/course_detail.html", context)


def module_detail(request, code):
    student = None
    if request.user.is_authenticated and not request.user.is_staff:
        student = request.user.student

    # Get module details and related registrations
    module = get_object_or_404(Module, code=code)
    context = {
        "title": "Modules",
        "registrations": module.module_registrations, 
        "module": module
        }
    if student:
        context["has_registered"]=student.registered_on_module(module)
        
    return render(request, "studentreg/module_detail.html", context)

# To register on a module (You have to be logged in)
@login_required
def module_register(request, code):
    
    # Get module and student details
    module = get_object_or_404(Module, code=code)
    student = request.user.student  # to fetch current logged in student

    if Registration.objects.filter(student=student, module=module).exists():
        messages.warning(request, "You are already registered for this module.")
    else:
        
        # Create a new registration
        Registration.objects.create(student=student, module=module)
        messages.success(
            request, f"You have successfully registered for {module.name}."
        )
    return redirect("studentreg:module_detail", code=code)


@login_required
def module_unregister(request, code):
    
    # Get module and student details
    module = get_object_or_404(Module, code=code)
    student = request.user.student  # to fetch current logged in student
    try:
        
        # Delete existing registration
        registration = Registration.objects.get(student=student, module=module)
        registration.delete()
    except Registration.DoesNotExist:
        messages.warning(request, "You are not registered on this module.")
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def my_registrations(request):
    
    # Get student's registrations and paginate them
    student = request.user.student  
    registrations = student.student_registrations.select_related('module').order_by('-date_of_registration')

    # Paginate the registrations
    paginator = Paginator(registrations, 3)  # Show 3 registrations per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'studentreg/my_registrations.html', {'page_obj': page_obj})

@login_required
def my_registration_page(request):
    student = request.user.student  # Assuming you have a related Student object for each User
    registrations = student.student_registrations.select_related('module').order_by('-date_of_registration')

    # Paginate the registrations
    paginator = Paginator(registrations, 2)  # Show 2 registrations per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'studentreg/my_registration_page.html', {'page_obj': page_obj})


class CustomPasswordResetView(PasswordResetView):
    # we still need to take care of when user puts in an incorrect email that doesn't exist
    # i think  django will not find the user by the incorrect email
    # so no email will get sent

    # Custom Password Reset View
    email_template_name = "auth/password_reset_email.html"
    subject_template_name = "auth/password_reset_subject.txt"
    template_name = "auth/password_reset_form.html"

    def get_success_url(self):
        return reverse("password_reset_done")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    # Custom Password Reset Done View
    template_name = "auth/password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    # Custom Password Reset Confirm View
    template_name = "auth/password_reset_confirm.html"

    # redirect to login page after successful password reset
    # we also need to show errors if user puts unmatching passwords
    def get_success_url(self):
        return reverse("login")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    
    # Custom Password Reset Complete View
    template_name = "auth/password_reset_complete.html"
    
