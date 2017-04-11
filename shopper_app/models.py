from __future__ import unicode_literals

from django.db import models

# imported so we can utilize named urls in urls.py
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse('item_view', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ShoppingListItem(models.Model):
    item = models.ForeignKey(Item, related_name='shopping_lists')
    shopping_list = models.ForeignKey(ShoppingList, related_name='items')

    def __str__(self):
        return self.shopping_list.name
