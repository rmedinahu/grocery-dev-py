from django.shortcuts import render

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














