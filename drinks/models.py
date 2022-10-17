from django.db import models

# Model inherits from Model class
class Drink(models.Model):
    # Specify model attributes
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    # Method to return Drink object as a string
    def __str__(self):
        return self.name + ' ' + self.description
