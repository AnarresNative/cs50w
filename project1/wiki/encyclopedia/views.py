from django.shortcuts import render
import os
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entry(request, title):
    return render(request, "encyclopedia/layout.html", {
        "title": title,
        "markdown": util.get_entry(title)
    })

