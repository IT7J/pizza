from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import RegularPizza, SicilianPizza, Toppings, Subs, Pasta, Salads, Dinnerplates, Cart

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "rpizzas": RegularPizza.objects.all(),
        "spizzas": SicilianPizza.objects.all(),
        "toppings": Toppings.objects.all(),
        "subs": Subs.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salads.objects.all(),
        "dinnerplates": Dinnerplates.objects.all()

    }
    return render(request, "menu/index.html", context)

def book_pasta(request, pasta_id):
    if request.method == 'POST':
       f = Cart.objects.create()
       pasta = Pasta.objects.get(pk = pasta_id)
       f.cartitems_pasta.add(pasta)
    return redirect('/')


def book_salad(request, salad_id):
    if request.method == 'POST':
       f = Cart.objects.create()
       salad = Salads.objects.get(pk = salad_id)
       f.cartitems_salads.add(salad)
    return redirect('/')



