from django.urls import path
from cr_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/<str:student_name>/', views.show_result, name='show_result'),
]

