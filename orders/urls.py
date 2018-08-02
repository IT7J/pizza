from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<int:pasta_id>/book_pasta", views.book_pasta, name = "book_pasta"),
    path("<int:salad_id>/book_salad", views.book_pasta, name = "book_salad")
]
