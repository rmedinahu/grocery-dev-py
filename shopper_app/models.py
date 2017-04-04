from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ShoppingListItem(models.Model):
    item = models.ForeignKey(Item)
    shopping_list = models.ForeignKey(ShoppingList)

    def __str__(self):
        return self.shopping_list.name
