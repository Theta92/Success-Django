from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


from .forms import (
    RegisterForm,
    UserUpdateForm,
    StudentProfileUpdateForm,
    StudentCreationForm,
)
from .models import Student, Module, Group


def home(request):
    courses = Group.objects.all()
    context = {"title": "Welcome", "courses": courses}
    return render(request, "studentreg/home.html", context)


def about(request):
    return render(request, "studentreg/about.html", {"title": "About"})


def contact(request):
    return render(request, "studentreg/contact.html", {"title": "Contact"})


def login(request):
    return render(request, "studentreg/login.html", {"title": "Login"})


def register(request):
    student_form = StudentCreationForm()
    register_form = RegisterForm()

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        student_form = StudentCreationForm(request.POST)

        if register_form.is_valid() and student_form.is_valid():
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


@login_required
def profile(request):
    if request.method == "POST":
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
        u_form = UserUpdateForm(instance=request.user)
        sp_form = StudentProfileUpdateForm(instance=request.user.student)
    context = {"u_form": u_form, "sp_form": sp_form, "title": "Student Profile"}
    return render(request, "studentreg/profile.html", context)


def course_detail(request, id):
    course = get_object_or_404(Group, id=id)
    context = {"title": "Modules", "course": course, "modules": course.modules.all()}
    return render(request, "studentreg/course_detail.html", context)


def module_detail(request, code):
    module = get_object_or_404(Module, code=code)
    context = {"title": "Modules", "module": module}
    return render(request, "studentreg/module_detail.html", context)
