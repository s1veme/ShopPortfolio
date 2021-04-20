from django.shortcuts import render
from rest_framework import generics
from .serializers import CategoryDeteilSerializer, CategoryListSerializer, ProductDeteilSerializer, ProductListSerializer
from .models import ProductCategory, Product
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny



#СОЗдАНИЕ КАТЕГОРИИ
class ProductCategoryView(generics.CreateAPIView):
    serializer_class = CategoryDeteilSerializer
    permission_classes = (IsAdminUser,)

#ПРОСМОТР КАТЕГОРИИ
class ProductCategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = ProductCategory.objects.all()
    permission_classes = (AllowAny,)

#РЕАЛИЗАЦИЯ GET, PUT, PATCH, DELETE КАТЕГОРИИ
class ProductCategoryDeteilView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDeteilSerializer
    queryset = ProductCategory.objects.all()


# СОЗдАНИЕ ПРОДУКТА
class ProductView(generics.CreateAPIView):
    serializer_class = ProductDeteilSerializer
    permission_classes = (AllowAny,)

#ПРОСМОТР ПРОДУКТА
class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)

#РЕАЛИЗАЦИЯ GET, PUT, PATCH, DELETE ПРОДУКТА
class ProductDeteilView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDeteilSerializer
    queryset = Product.objects.all()
