from django.db import models
from datetime import datetime

class Good(models.Model):
    name = models.CharField("Назва товару", max_length=50)
    price = models.IntegerField("Ціна товару", max_length=12)
    color = models.CharField("Колір", max_length=20)
    description = models.TextField("Опис товару", max_length=250)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name