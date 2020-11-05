"""turismo_real URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.accounts.views import user_register
from apps.accounts.views import user_login
from apps.accounts.views import user_logout
from apps.bookings.views import index
from apps.apartments.views import register_apartment
from apps.extra_services.views import register_extra_service


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('apartment/register', register_apartment, name='register_apartment'),
    path('extra_services/register', register_extra_service, name='register_extra_service')
]
