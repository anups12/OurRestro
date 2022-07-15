from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('message/', views.Message, name='message'),
    path('add/', views.AddProduct, name='add'),
    path('register/', views.Register, name='register'),
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogout, name='logout'),
    path('add_to_cart/', views.AddToCart, name='add_to_cart'),
]