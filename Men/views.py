from django.shortcuts import render
from django.views.generic import ListView,DeleteView,View
from .models import Men_Item
# Create your views here.

class indexview(ListView):
    model = Men_Item
    paginate_by = 15
    template_name = "index.html"