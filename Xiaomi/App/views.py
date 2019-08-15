from django.shortcuts import render
from App.models import Index, Paymenu


# Create your views here.


def index(request):
    menus = Index.objects.all()
    title = Paymenu.objects.all()

    return render(request, "index.html", context={"menus": menus, 'title': title})
