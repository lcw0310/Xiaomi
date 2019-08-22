import re

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from App.models import Index, Paymenu, List, Detail, Cart


# Create your views here.


def index(request):
    menus = Index.objects.all()
    title = Paymenu.objects.all()
    return render(request, "index.html", context={"menus": menus, 'title': title})


def search(request):
    if request.method == 'POST':
        canshu = request.POST.get('shousuo')
        list = Index.objects.all()
        return render(request, "search_list.html", {'canshu': canshu, 'lists': list})
    return HttpResponseRedirect('/index/')


def list(request):
    title = Paymenu.objects.all()
    list = List.objects.all()
    return render(request, 'list.html', {'titles': title, 'lists': list})


def detail(request):
    detail = Index.objects.all()
    image = Detail.objects.all()
    id = request.GET.get('id')
    parameter = int(id)
    return render(request, 'details.html', context={'details': detail, 'parameter_id': parameter, 'image': image})


def shopping_cart(request):
    commodity = Index.objects.all()
    id = request.GET.get('id')
    parameter = int(id)
    for vaule in commodity:
        if parameter == vaule.id:
            a = Cart.objects.filter(id=vaule.id)
            if not len(a) == 0: #判断列表不为空
                cart = Cart.objects.get(id=vaule.id)
                cart.digital += 1
                cart.save()
            else:
                add_cart = Cart(image=vaule.image, title=vaule.title, price=vaule.price)
                add_cart.save()
    cart = Cart.objects.all()
    return render(request, 'shopping_cart.html', {'commodity': cart})

def delete(request):


def settlement(request):
    return render(request, 'settlement.html')
