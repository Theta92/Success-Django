from django.shortcuts import render


def home(request):
    return render(request, "studentreg/home.html", {"title": "Welcome"})


def about(request):
    return render(request, "studentreg/about.html", {"title": "About"})


def contact(request):
    return render(request, "studentreg/contact.html", {"title": "Contact"})


def login(request):
    return render(request, "studentreg/login.html", {"title": "Login"})


def register(request):
    return render(request, "studentreg/register.html", {"title": "Register"})


def modules(request):
    return render(request, "studentreg/modules.html", {"title": "Modules"})
