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

        full_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        send_mail(
            subject="New Contact Message",
            message=full_message,
            from_email=email,
            recipient_list=['shirishsomase@gmail.com'],
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')