from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Just print (for testing)
        print("New Contact Message")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')