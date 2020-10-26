from django.shortcuts import render
from .models import Dataset

# Create your views here.
def index(request):
    context = {'datasets': Dataset.objects.all()}
    return render(request, 'main/index.html', context)
