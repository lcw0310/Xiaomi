from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list$',views.list,name='list'),
    url(r'^detail$',views.detail,name='detail'),
    url(r'shopping_cart',views.shopping_cart,name='shopping_cart'),
    url(r'settlement',views.settlement,name='settlement')
]
