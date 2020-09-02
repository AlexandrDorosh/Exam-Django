from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.products, name="products"),
    path('special_offer/', views.special_offer, name="special offer"),
    path('product_details/', views.product_details, name="product details"),
    path('compair/', views.compair, name="product compair"),
    path('summary/', views.summary, name="product summary"),
    path('login/', views.login, name="login"),
    path('forgetpass/', views.forgetpass, name="forget password"),
    path('register/', views.register, name="register"),
    path('contact/', views.contact, name="contact us"),
    path('normal/', views.normalinfo, name="normal information"),
    path('faq/', views.faq, name="faq"),
]