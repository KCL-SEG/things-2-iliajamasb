from django.shortcuts import render
from .forms import registerThing

def home(request):
    form = registerThing()
    return render(request, 'home.html', {'form': form})
