from django.contrib import admin
from django.urls import path, include
from . import views 


from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('', include('django.contrib.auth.urls')),
]
