from django.shortcuts import render
from rest_framework import generics
from . serializers import CategoryDeteilSerializer, CategoryListSerializer, ProductDeteilSerializer, ProductListSerializer
from . models import ProductCategory, Product
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView



#СОЗдАНИЕ КАТЕГОРИИ
class ProductCategoryView(generics.CreateAPIView):
    serializer_class = CategoryDeteilSerializer

#ПРОСМОТР КАТЕГОРИИ
class ProductCategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = ProductCategory.objects.all()
    #permission_classes = (IsAuthenticated,)

#РЕАЛИЗАЦИЯ GET, PUT, PATCH, DELETE КАТЕГОРИИ
class ProductCategoryDeteilView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDeteilSerializer
    queryset = ProductCategory.objects.all()


#СОЗдАНИЕ ПРОДУКТА
class ProductView(generics.CreateAPIView):
    serializer_class = ProductDeteilSerializer

#ПРОСМОТР ПРОДУКТА
class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    #permission_classes = (IsAdminUser,)

#РЕАЛИЗАЦИЯ GET, PUT, PATCH, DELETE ПРОДУКТА
class ProductDeteilView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDeteilSerializer
    queryset = Product.objects.all()
