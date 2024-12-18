from django.shortcuts import render
import os
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entry(request, title):
    if util.get_entry(title) is not None:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "markdown": util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/missing_entry.html", {
            "title": title
        })

