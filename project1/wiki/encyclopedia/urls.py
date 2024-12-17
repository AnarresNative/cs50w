from django.urls import path

from . import views, util

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_entry, name="wiki")
]
