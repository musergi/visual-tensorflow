from django.contrib import admin
from .models import Dataset, TensorflowModel

admin.site.register(Dataset)
admin.site.register(TensorflowModel)
