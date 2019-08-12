from django.shortcuts import render
from App.models import Index

# Create your views here.


def index(request):
    menus = Index.objects.all()
    print(menus)
    return render(request, "index.html", context={"menus": menus})
