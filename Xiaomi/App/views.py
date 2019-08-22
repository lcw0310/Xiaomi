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


# def shopping_cart(request):
#     commodity = Index.objects.all()
#     id = request.GET.get('id')
#     # parameter = int(id)
#     for value in commodity:
#         value_id = str(value.id)
#         if id == value_id:
#             cart_id = Cart.objects.filter(id=value.id)
#             if not len(cart_id) == 0: #判断列表不为空
#                 cart = Cart.objects.get(id=value.id)
#                 cart.digital += 1
#                 cart.save()
#             else:
#                 add_cart = Cart(image=value.image, title=value.title, price=value.price)
#                 add_cart.save()
#     cart = Cart.objects.all()
#     return render(request, 'shopping_cart.html', {'commodity': cart})
def shopping_cart(request):
    commodity = Index.objects.all()
    title = request.GET.get('tit')
    for value in commodity:
        value_title = str(value.title)
        if title == value_title:
            cart_id = Cart.objects.filter(title=value.title)
            if not len(cart_id) == 0: #判断列表不为空
                cart = Cart.objects.get(title=value.title)
                cart.digital += 1
                cart.save()
            else:
                add_cart = Cart(image=value.image, title=value.title, total_price=value.price)
                add_cart.save()
    cart = Cart.objects.all()
    if len(cart) == 0:
        return render(request,'shopping_null.html')
    return render(request, 'shopping_cart.html', {'commodity': cart})

def delete(request):
    id = request.GET.get('id')
    cart = Cart.objects.filter(id=id)
    parameter = int(id)
    print(parameter)
    for cart_id in cart:
        print(cart_id.id)
        if parameter == cart_id.id:
            cart.delete()
        return HttpResponseRedirect('/index/')

def settlement(request):
    return render(request, 'settlement.html')
