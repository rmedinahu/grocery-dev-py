from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView

class HomeView(TemplateView):
    """Home page
    url: /, name: home
    """
    template_name = 'home.html'