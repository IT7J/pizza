from django.contrib import admin

from .models import RegularPizza, SicilianPizza, Toppings, Subs, Pasta, Salads, Dinnerplates, Cart, Menu

admin.site.register(Menu)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(Salads)
admin.site.register(Dinnerplates)
admin.site.register(Cart)
admin.site.register(Pasta)

# Register your models here.
