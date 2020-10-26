from django.shortcuts import render
from .models import Dataset, TensorflowModel

# Create your views here.
def index(request):
    context = {
        'datasets': Dataset.objects.all(),
        'models': TensorflowModel.objects.all()
    }
    return render(request, 'main/index.html', context)
