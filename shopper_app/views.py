from django import forms
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.views.generic import TemplateView, DetailView, ListView, \
                                     CreateView, UpdateView, FormView

from .models import Item, ShoppingList, ShoppingListItem

##### Form classes ####
class UploadFileForm(forms.Form):
    file = forms.FileField()

class SearchForm(forms.Form):
    search = forms.CharField()

##### Data handlers #####
def handle_file_data(file):
    print file.read()

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
        # variables in context list. E.g., only show type listed in query
        # param if it is part of the url request.

        # Query param exists if: /item/?filter=meat or other type name.

        filter_val = self.request.GET.get('filter')
        if filter_val:
            context['object_list'] = Item.objects.filter(item_type=filter_val)
        

        item_types = set()
        for i in Item.objects.all().values('item_type'):
            item_types.add(i.values()[0])

        context['types'] = list(item_types)
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

        return context


class UploadShoppingListView(FormView):
    template_name = 'shopping_list_file_upload.html'
    form_class = UploadFileForm  # see UploadFileForm class above.
    success_url = '/'           

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        file = self.request.FILES['file']
        handle_file_data(file)
        return super(UploadShoppingListView, self).form_valid(form)   


class SearchView(FormView):
    template_name = 'search.html'
    form_class = SearchForm  # see SearchForm class above.

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It returns an HttpResponse containing search results.
        
        # get the search term entered in the search form
        search_term = form.cleaned_data['search']
        
        # search for items where name is LIKE search term
        context = self.get_context_data()     
        context['results'] = Item.objects.filter(name__contains=search_term)
        return render(self.request, self.template_name, context)
        






