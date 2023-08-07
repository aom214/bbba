from django.contrib import admin
from django.urls import path
from harryshop import views

urlpatterns = [
    path('',views.shop,name='home'),
    path('cart/<str:product_id>/',views.removeproduct,name='cart'),
    path('<str:product_cate>/<str:product_id>/',views.products,name='product'),
    path('addtocart/<str:product_id>/',views.addtocart,name='addcart'),
    path('cart/',views.cart,name='cart'),
]