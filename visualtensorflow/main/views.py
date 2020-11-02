from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dataset, TensorflowModel


def index(request):
    context = {
        'datasets': Dataset.objects.all(),
        'models': TensorflowModel.objects.all()
    }
    return render(request, 'main/index.html', context)


def network_training(request, model_id: int, dataset_id: int):
    dataset = Dataset.objects.get(id=dataset_id)
    model = TensorflowModel.objects.get(id=model_id)
    model.start_training(dataset)
    return redirect('index')
