from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name="index"),
    path("title",views.title_search, name="title"),
    path("authors",views.author_search,name="authors"),
    path("categories", views.categories_search, name="categories")
]
