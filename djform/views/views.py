from django.shortcuts import render
from djform.forms.forms import InputForms


def form_view(request):
    form = InputForms()
    if request.method == 'POST':
        form = InputForms(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'djform/form.html', {'form': form})
# Create your views here.
