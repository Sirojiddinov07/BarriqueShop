from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logoutUser, name='logout'),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('shop/', shop, name='shop'),
    path('shop_cart/', shop_cart, name='shop_cart'),
    path('add_cart/<int:pk>/', add_cart, name='add_cart'),
    path('del_cart/<int:pk>/', del_cart, name='del_cart'),
    path('shop_list/', shop_list, name='shop_list'),
    path('shop_single/<int:pk>/', shop_single, name='shop_single'),
    path('shop_checkout/', shop_checkout, name='shop_checkout'),
    path('blog_single/<int:pk>/', blog_single, name='blog_single'),

    path('contact/', contact, name='contact'),

]
