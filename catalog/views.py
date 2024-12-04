from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from catalog.models import Product


class HomeView(ListView):
    model = Product



def contacts(request):
    return render(request, "contacts.html")

class ProductDetailView(DetailView):
    model = Product
