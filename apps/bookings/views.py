from django.shortcuts import render, redirect
from apps.apartments.models import Apartment, ApartmentImage
from django.http import JsonResponse
from django.http import HttpResponse


def index(request):
    apartments = Apartment.objects.all()
    data = []

    for apartment in apartments.iterator():
        apartment_image_object = ApartmentImage.objects.filter(apartment_id=apartment.id).first()
        apartment_data_image = {}
        apartment_data_image['apartment'] = apartment
        apartment_data_image['apartment_image'] = apartment_image_object
        data.append(apartment_data_image)

    context = {
        'data': data
    }
    return render(request, 'index.html', context)

def book_apartment(request, apartment_id):

    apartment = Apartment.objects.get(id=apartment_id)
    apartment_images = ApartmentImage.objects.filter(apartment_id=apartment.id)
    context = {
        'apartment': apartment,
        'apartment_images': apartment_images
    }
    return render(request, 'bookings/book_apartment.html', context)

def check_availability(request):
    check_in_date = request.POST.get("check_in_date")
    check_out_date = request.POST.get("check_out_date")
    number_guests = request.POST.get("number_guests")
    print(check_in_date)
    if 1==1:
        if request.is_ajax():
            availability_response = {'check_in_date': check_in_date, 'check_out_date': check_out_date, 'number_guests': number_guests };
            return JsonResponse(availability_response, status=200)
        else:
            message = "Not ajax"
            return HttpResponse(status=500)
    else:
        message = "You must provide dates!"
        return HttpResponse(status=500)


def booking_confirm(request):
    if request.method == 'POST':
        check_in_date = request.POST.get('check-in-date')
        context = {}
        return render(request, 'bookings/booking_confirm.html', context)
