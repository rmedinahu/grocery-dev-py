"""grocerysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from shopper_app.views import HomeView, ItemListView, ItemCreateView, \
    ItemDetailView, ItemUpdateView, AddShoppingListItemView, \
    ShoppingListItemsView, ShoppingListItemsAllView, UploadShoppingListView, \
    SearchView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),

    # show all item object in the db.
    url(r'^items/$', ItemListView.as_view(), name='item_list'),
    
    # url pattern for showing the create item page.
    url(r'^item/add/$', ItemCreateView.as_view(), name='item_add'),

    # using a named url parameter (pk must match one or more digits) to retrieve correct object from database.
    url(r'^item/edit/(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='item_edit'),

    # using a named url parameter (pk must match one or more digits) to retrieve correct object from database.
    url(r'^item/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item_view'),

    # url to list all shopping lists.
    url(r'^shopping-lists/$', ShoppingListItemsAllView.as_view(), name='shopping_lists_all'),    

    # url for viewing items in a shopping list
    url(r'^shopper/(?P<shopping_list_pk>\d+)/$', ShoppingListItemsView.as_view(), name='shopping_list_items_view'),


    # url pattern for adding an item to a shopping list.
    # uses named regex groups to collect multiple parameters
    url(r'^shopper/(?P<shopping_list_pk>\d+)/add/$', AddShoppingListItemView.as_view(), name='add_shoppinglist_item'),

    url(r'^shopper/upload/$', UploadShoppingListView.as_view(), name='upload_shoppinglist_item'),

    url(r'^search/$', SearchView.as_view(), name='search'),

    # admin site.
    url(r'^admin/', admin.site.urls),
]













