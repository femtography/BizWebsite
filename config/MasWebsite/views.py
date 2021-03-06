from django.shortcuts import render
from MasWebsite.models import Product, Sale

def index (request):
    featured_prod = Product.objects.all().filter(is_featured=True)
    active_i = featured_prod[0].name
    featured_sale = Sale.objects.all()
    return render(request, 'MasWebsite/index.html', {"ProdList": featured_prod, "ActiveImage": active_i, 'SaleTime': featured_sale})

def about(request):
    return render(request, 'MasWebsite/about.html')

def product(request, product_name):
    prod = Product.objects.get(name = product_name)
    return render(request, 'MasWebsite/product.html', {'Product': prod})

def shoppe(request, product_type):
    if product_type == 'all':
        featured_prod = Product.objects.all().order_by('name')
        return render(request, 'MasWebsite/shoppe.html', {"ProdList": featured_prod})

    featured_prod = Product.objects.all().filter(category=product_type).order_by('name')
    return render(request, 'MasWebsite/shoppe.html', {"ProdList": featured_prod})

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
