from django.shortcuts import render

def home(request):
    return render(request, 'studentreg/home.html')
def about(request):
    return render(request, 'studentreg/about.html')
def contact(request):
    return render(request, 'studentreg/contact.html')

# Create your views here.
