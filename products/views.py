from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#importing loading from django template
from django.template import loader
from .models import Product


def index(request):
	prod_fetch = Product.objects.all()
	return render(request, 'index.html', {'obj': prod_fetch})
