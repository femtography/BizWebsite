from django.urls import path

from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('product/<str:product_name>', views.product, name='product'),
    path('about', views.about, name='about'),
    path('shoppe', views.shoppe, name='shoppe'),
    path('', views.index, name='home'),
]
