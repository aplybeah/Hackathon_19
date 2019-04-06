from django.urls import path
from . import views

urlpatterns =[
    path("", views.homepage, name='homepage'),
    path("search/", views.search_page, name="search_page"),
    path("search/<int:id>", views.search_result, name="search_result")

]