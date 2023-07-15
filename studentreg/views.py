from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, 


def home(request):
    return render(request, "studentreg/home.html", {"title": "Welcome"})


def about(request):
    return render(request, "studentreg/about.html", {"title": "About"})


def contact(request):
    return render(request, "studentreg/contact.html", {"title": "Contact"})


def login(request):
    return render(request, "studentreg/login.html", {"title": "Login"})


def register(request):
    # student_form = StudentCreationForm()
    register_form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Your account has been created! Now you can login!"
            )
            return redirect("login")
        else:
            messages.warning(request, f"Unable to create account!")
    else:
        form = RegisterForm()

    return render(
        request,
        "studentreg/register.html",
        {
            "title": "Register",
            "register_form": register_form,
            #  "student_form": student_form
        },
    )


def modules(request):
    return render(request, "studentreg/modules.html", {"title": "Modules"})
