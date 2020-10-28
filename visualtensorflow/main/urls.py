from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('model/<int:model_id>/train/<int:dataset_id>/', views.network_training, name='train'),
]
