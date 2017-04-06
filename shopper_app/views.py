from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView

from .models import Item, ShoppingList, ShoppingListItem


class HomeView(TemplateView):
    """Home page
    url pattern: / name: home
    """
    template_name = 'home.html'


class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'

    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        context['object_list'] = Item.objects.filter(item_type='meat')
        context['fav_person'] = 'Trumpster';
        return context
    












