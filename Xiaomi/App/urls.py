from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list$', views.list, name='list'),
    url(r'^detail$', views.detail, name='detail'),
    url(r'^shopping_cart$', views.shopping_cart, name='shopping_cart'),
    url(r'^settlement$', views.settlement, name='settlement'),
    url(r'^search$', views.search, name='search'),
    # url(r'^add_cart$',views.add_cart,name='add_cart'),
    url(r'^delete$',views.delete,name='delect'),
]
