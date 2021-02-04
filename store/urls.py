from django.urls import path
from . import views


urlpatterns=[

    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('blog/',views.blog,name='blog'),
    path('arab/',views.arab,name='arab'),
    # path('detaile/',views.detaile,name='detaile'),
    path('checkout/',views.checkout,name='checkout'),
    path('update_item/',views.updateItem,name='update_item'),
    path('process_order/',views.processOrder,name='process_order'),


]