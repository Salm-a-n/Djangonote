from django.urls import path
from water_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_water, name='addwater'),
    path('list/', views.waterlist, name='waterlist'),
    path('edit/<int:pk>/', views.edit_intake, name='editwater'),
    path('delete/<int:pk>/', views.delete_intake, name='deletewater'),
    path('difference/', views.intake_difference, name='intake_difference'),

]
