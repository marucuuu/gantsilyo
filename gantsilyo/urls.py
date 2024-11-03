from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),

    path('product/', views.product, name='product'),
    path('about/', views.about, name='about'),



    # admin view urls start 

    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_user/', views.admin_adduser, name='admin_adduser'),
    path('add_product/', views.admin_addproduct, name='admin_addproduct'),

    # admin view urls start 
    
]