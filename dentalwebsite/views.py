from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Form
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['your-name']
        number = request.POST['your-phone']
        email = request.POST['your-email']
        address = request.POST['your-address']
        schedule = request.POST['your-schedule']
        time = request.POST['your-time']
        message = request.POST['your-message']

        # database
        Form.objects.create(name=name,number=number,email=email)
        context = {
            "name": name,
            "number": number,
            "email": email,
            "address": address,
            "schedule": schedule,
            "time": time,
            "message": message
        }
        messages = f'''
            Name: {name}
            Number: {number}
            Address: {address}
            Schedule: {schedule}
            Time: {time}
            Message: {message}
        '''

        #send_mail(f"From {name}", messages, email, ['yebes77@gmail.com'])
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        context = {
            "message_name": message_name,
            "message_email": message_email,
            "message": message,
        }
        send_mail(f"from {message_name}", message, message_email, ['yebes77@gmail.com'])

        return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html')