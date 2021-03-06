from django.shortcuts import render

from homepage.models import Input
from homepage.forms import AddTextForm

import subprocess

# Create your views here.
def index(request):
    if request.method == "POST":
        form = AddTextForm(request.POST)
        form.save()
        text = Input.objects.all().last().text
        out = subprocess.check_output(['cowsay', text], text=True)
        return render(request, "index.html", {"form": form, "out": out})

    form = AddTextForm()
    return render(request, "index.html", {"form": form})

def history(request):
    input = Input.objects.all()[::-1][0:10]
    return render(request, "history.html", {"input": input})    