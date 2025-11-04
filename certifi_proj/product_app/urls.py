# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),
    path('products/download-all/', views.download_all_products_pdf, name='download_all_products_pdf'),
    path('products/send-all/', views.send_all_products_email, name='send_all_products_email'),
]