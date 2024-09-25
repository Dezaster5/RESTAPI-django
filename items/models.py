from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название предмета")
    description = models.TextField(blank=True, null=True, verbose_name="Описание предмета")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена предмета")  
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    def __str__(self):
        return self.name
