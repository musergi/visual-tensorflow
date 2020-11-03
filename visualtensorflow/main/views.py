from django.http import request
from django.shortcuts import render, redirect
from tensorflow.python.eager.context import context
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

def network_choose_dataset(request, model_id: int):
    context = {
        'datasets': Dataset.objects.all()
    }
    return render(request, 'main/choose_dataset.html', context)


def network_details(request, model_id: int):
    model = TensorflowModel.objects.get(id=model_id)
    context = {
        'model': model.to_dict()
    }
    return render(request, 'main/model_details.html', context)