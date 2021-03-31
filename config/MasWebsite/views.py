from django.shortcuts import render

def index (request):
    return render(request, 'MasWebsite/index.html')

def about(request):
    return render(request, 'MasWebsite/about.html')

def shoppe(request):
    return render(request, 'MasWebsite/shoppe.html')

def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['user_name']
        email = request.POST['user_email']
        category = request.POST['category']

        subject = name.capitalize() + ' is reaching out from ' + email + ' about ' + category

        send_mail(subject,
        message,
        settings.EMAIL_HOST_USER,
        ['gcflores0303@gmail.com'],
        fail_silently=False)

    return render(request, 'MasWebsite/contact.html')
