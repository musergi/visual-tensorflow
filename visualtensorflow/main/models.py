import pickle
from threading import Thread
import tensorflow as tf
from django.db import models

# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=200)
    data_file = models.FileField(upload_to='datasets/')

    def load(self):
        with self.data_file.open('rb') as dataset_file:
            return pickle.load(dataset_file)

class TensorflowModel(models.Model):
    name = models.CharField(max_length=200)
    model_file = models.FileField(upload_to='models/')

    def start_training(self, dataset: Dataset):
        # TODO: Check
        Thread(
            target=lambda: self._train(dataset),
            daemon=False).run()

    def _train(self, dataset: Dataset):
       (x_train, y_train), (x_test, y_test) = dataset.load() 
       model = self.load()
       model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
       model.fit(x_train, y_train, epochs=1)
       model.evaluate(x_test, y_test, verbose=2)

    def _load(self) -> tf.keras.Model:
        with self.model_file.open('r') as f:
            return tf.keras.models.model_from_json(f.read())

    def to_dict(self) -> dict:
        tf_model = self._load()
        return {
            'input_shape': str(tf_model.input_shape),
            'output_shape': str(tf_model.output_shape),
            'layers': [self._layer_to_dict(layer) for layer in tf_model.layers]
        }
    
    @staticmethod
    def _layer_to_dict(layer: tf.keras.layers.Layer):
        return {
            'name': layer.name,
            'input_shape': layer.input_shape,
            'output_shape': layer.output_shape
        }
