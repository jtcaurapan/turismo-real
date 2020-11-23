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
from apps.bookings.views import check_availability
from apps.apartments.views import register_apartment
from apps.apartments.views import edit_apartment
from apps.apartments.views import apartment_list
from apps.bookings.views import book_apartment
from apps.bookings.views import booking_confirm
from apps.extra_services.views import register_extra_service
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('apartment/register', register_apartment, name='register_apartment'),
    path('extra_services/register', register_extra_service, name='register_extra_service'),
    path('book/apartment/<int:apartment_id>/', book_apartment, name="book_apartment"),
    path('booking/confirm/', booking_confirm, name="booking_confirm"),
    path('apartment/edit/<int:apartment_id>/', edit_apartment, name="edit_apartment"),
    path('apartment/list/', apartment_list, name="apartment_list"),
    path('check-availability/', check_availability, name='check_availability'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
