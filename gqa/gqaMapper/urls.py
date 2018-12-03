from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'qgaMapper'
urlpatterns = [
    path("", views.index, name = "index"),
    path("search", views.search, name = "search"), #Homepage->Search
    path("help", views.help, name = "help"), #Homepage->Help
]