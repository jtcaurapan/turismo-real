from django.shortcuts import render
from .forms import ExtraServiceForm

def register_extra_service(request):
    if request.method == 'POST':
        form = ExtraServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = ExtraServiceForm()
    context = {'form': form}

    return render(request, 'extra_services/register_extra_service.html', context)
