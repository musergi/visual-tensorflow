from django.db import models

# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=200)
    data_file = models.FileField(upload_to='datasets/')

class TensorflowModel(models.Model):
    name = models.CharField(max_length=200)
    model_file = models.FileField(upload_to='models/')
