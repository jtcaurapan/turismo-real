from .forms import ApartmentForm
from .forms import ApartmentImageForm
from .models import Apartment
from .models import ApartmentImage
from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.forms import inlineformset_factory

def register_apartment(request):
    apartment_form = ApartmentForm()
    apartmentImageFormSet = formset_factory(ApartmentImageForm, extra=4)

    if request.method == 'POST':
        apartment_form = ApartmentForm(request.POST, request.FILES)
        formset = apartmentImageFormSet(request.POST, request.FILES)

        if apartment_form.is_valid():
            if formset.is_valid():
                ApartmentFormInstance = apartment_form.save()

                for i in formset:
                    formsetInstance = i.save(commit=False)
                    formsetInstance.apartment_id = ApartmentFormInstance.id
                    formsetInstance.save()

                return redirect('index')

    context = {
        'apartment_form': apartment_form,
        'apartmentImageFormSet': apartmentImageFormSet
    }

    return render(request, 'apartments/register_apartment.html', context)


def apartment_list(request):
    apartments = Apartment.objects.all()
    context = {'apartments': apartments}
    return render(request, 'apartments/apartment_list.html', context)


def edit_apartment(request, apartment_id):

    instance= Apartment.objects.get(id=apartment_id)
    apartment_form = ApartmentForm(instance=instance)

    apartmentImageFormSet = formset_factory(ApartmentImageForm, extra=4)

    if request.method == 'POST':
        apartment_form = ApartmentForm(request.POST)
        formset = apartmentImageFormSet(request.POST, request.FILES)

        if apartment_form.is_valid():
            if formset.is_valid():
                apartment_form.save()
                for i in formset:
                    i.save()
                return redirect('index')

    context = {
        'apartment_form': apartment_form,
        'apartmentImageFormSet': apartmentImageFormSet
    }

    return render(request, 'apartments/register_apartment.html', context)
