from django.shortcuts import render
from django.urls import reverse

from django.views.generic import TemplateView, DetailView, ListView, \
                                     CreateView, UpdateView

from .models import Item, ShoppingList, ShoppingListItem


class HomeView(TemplateView):
    """ Home page
    url pattern: / name: home
    """
    template_name = 'home.html'


class ItemListView(ListView):
    """ Show list of items in database.
    url pattern: /items name: item_list
    """
    model = Item
    template_name = 'item_list.html'

    def get_context_data(self, **kwargs):
        """ Override ListView method to set custom template variables.
        """
        # get the parent context list.
        context = super(ItemListView, self).get_context_data(**kwargs)
        
        # set custom template variables by adding or over writing 
        # variables in context list. E.g., only show meat types.
        context['object_list'] = Item.objects.filter(item_type='meat')

        # make sure to return the variable list.
        return context


class ItemDetailView(DetailView):
    """ Show a page containing information about an Item object. Using
    this view requires the url pattern have a variable named "pk".
    url pattern: item/(?P<pk>\d+) name: item_view
    """
    model = Item
    template_name = 'item.html'


class ItemCreateView(CreateView):
    """ Show a page containing a form for adding a new Item object.
    url pattern: /item/add name: item_add
    """
    model = Item
    template_name = 'item_create.html'
    fields = ['name', 'item_type', 'price']


class ItemUpdateView(UpdateView):
    """ Show a page containing a form for adding a new Item object.
    url pattern: /item/edit/(?P<pk>\d+) name: item_edit
    """
    model = Item
    template_name = 'item_edit.html'
    fields = ['name', 'item_type', 'price']


class ShoppingListItemsAllView(ListView):
    model = ShoppingList
    template_name = 'shopping_list_all.html'


class ShoppingListItemsView(TemplateView):
    """ Show a page containing information about items in a shopping list. Using
    this view requires the url pattern have a variable named "shopping_list_pk".
    url pattern: shopper/(?P<shopping_list_pk>\d+) name: shopping_list_items_view
    """
    template_name = 'shopping_list_items.html'

    def get_context_data(self, **kwargs):
        # get the parent context list.
        context = super(ShoppingListItemsView, self).get_context_data(**kwargs)
        
        # get the shopping list object
        shoplist = ShoppingList.objects.get(pk=self.kwargs.get('shopping_list_pk'))

        # get the items associated with the shopping list
        shopitems = shoplist.items.all()
        
        context['shopitems'] = shopitems
        context['shoplist'] = shoplist
        return context


class AddShoppingListItemView(CreateView):
    """ Show a page containing a form for adding and Item object
    to a ShoppingList object
    url pattern: /shopper/(?P<shopping_list_pk>\d+)/add name: add_shoppinglist_item
    """
    model = ShoppingListItem
    template_name = 'shopping_list_item_add.html'
    fields = ['shopping_list', 'item']

    def get_success_url(self):
        print self.get_object().shopping_list
        return reverse('home')

    def get_initial(self):
        # assign values to form
        initial = super(AddShoppingListItemView, self).get_initial()
        initial['shopping_list'] = ShoppingList.objects.get(pk=self.kwargs.get('shopping_list_pk'))
        return initial

    def get_context_data(self, **kwargs):
        """ Override CreateView method to set custom template variables.
        """
        # get the parent context list.
        context = super(AddShoppingListItemView, self).get_context_data(**kwargs)
        context['shopping_list'] = ShoppingList.objects.get(pk=self.kwargs.get('shopping_list_pk'))

        # Demo
        context['kwargs'] = self.kwargs
        return context








