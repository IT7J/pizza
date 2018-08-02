from django.db import models
from django.contrib.auth.models import User


class RegularPizza(models.Model):
      pizza = models.CharField(max_length=64)
      small = models.FloatField()
      large = models.FloatField()

      def __str__(self):
        return f"{self.pizza} {self.small}$ {self.large}$"

class SicilianPizza(models.Model):
      pizza = models.CharField(max_length=64)
      small = models.FloatField()
      large = models.FloatField()

      def __str__(self):
        return f"{self.pizza} {self.small}$ {self.large}$"



class Toppings(models.Model):
      toppings = models.CharField(max_length=64)

      def __str__(self):
        return f"{self.toppings}"


class Subs(models.Model):
      sub = models.CharField(max_length=64)
      small = models.FloatField(null =  True, blank = True)
      large = models.FloatField()

      def __str__(self):
        return f"{self.sub} {self.small}$ {self.large}$"


class Pasta(models.Model):
      pasta = models.CharField(max_length=64)
      price = models.FloatField()

      def __str__(self):
        return f"{self.pasta} {self.price}$"



class Salads(models.Model):
      salad = models.CharField(max_length=64)
      price = models.FloatField()

      def __str__(self):
        return f"{self.salad} {self.price}$"


class Dinnerplates(models.Model):
      dinnerplate = models.CharField(max_length=64)
      small = models.FloatField()
      large = models.FloatField()

      def __str__(self):
        return f"{self.dinnerplate} {self.small}$ {self.large}$"


class Menu(models.Model):
      pastaf = models.ForeignKey(Pasta, on_delete = models.CASCADE, related_name="menu_pasta")


class Cart(models.Model):
      cartitems_pasta= models.ManyToManyField(Pasta, blank=True, related_name="cart")
      cartitems_salads = models.ManyToManyField(Salads, blank = True, related_name = "cart1")





# Create your models here.
