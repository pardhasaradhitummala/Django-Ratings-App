from django.urls import path
from .views import *

urlpatterns = [
    path('',user_login),
    path('registerpage',user_register,name="register"),
    path('registeruser',user_registering),
    path('loginuser',login_user),
    path('moviedata/<int:id>',moviedata),
    path('moviedata/saverating/<int:id>',save_rating)
]