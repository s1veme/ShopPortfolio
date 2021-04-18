from django.contrib import admin
from django.urls import path, include
from shop.views import *


app_name = 'shop'
urlpatterns = [
    # path('shop/create/category', ProductCategoryView.as_view()),
    # path('all/category', ProductCategoryListView.as_view()),
    # path('shop/detail/category/<int:pk>', ProductCategoryDeteilView.as_view()),

    # path('shop/create/product', ProductView.as_view()),
    path('all/products', ProductListView.as_view()),
    # path('shop/detail/product/<int:pk>', ProductDeteilView.as_view()),
]
