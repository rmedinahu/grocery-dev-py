from django.contrib import admin

# Register your models here.
# E.g., admin.site.register(modelnamehere)

from .models import Item, ShoppingList, ShoppingListItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_type', 'price')
    list_filter = ('item_type',)

class ShoppingListItemAdmin(admin.ModelAdmin):
    list_display = ('shopping_list', 'item')
    list_filter = ('shopping_list',)


admin.site.register(Item, ItemAdmin)
admin.site.register(ShoppingList)
admin.site.register(ShoppingListItem, ShoppingListItemAdmin)