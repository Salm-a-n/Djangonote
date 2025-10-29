from django.urls import path
from . import views

urlpatterns=[
    path('create/',views.create_book, name='create_book'),
    path('read/',views.all_data,name='home'),
    path('update/<int:id>/',views.update_book,name='update_book'),
    path('delete/<str:title>/',views.delete_book,name='delete_book')
]