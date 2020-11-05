from .forms import ApartmentForm
from django.shortcuts import render, redirect

def register_apartment(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = ApartmentForm()
    context = {'form': form}
    return render(request, 'apartments/register_apartment.html', context)

