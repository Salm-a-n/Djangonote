from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product),
    path('all/', views.list_products),
    path('update/<int:pk>/', views.update_product),
    path('delete/<int:pk>/', views.delete_product),
]