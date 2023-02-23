from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from .models import Product, ProductCategory, Results
from .serializers import (
    ProductListSerializer, ProductDetailSerializer,
    ProductCategorySerializer, ProductResultSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category")
    list_serializer_class = ProductListSerializer
    serializer_class = ProductDetailSerializer
    filterset_fields = ["category_id", "is_top"]
    http_method_names = ["get"]

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class
        return self.serializer_class

    def get_object(self):
        obj = super().get_object()
        if obj.results_set.count() == 0:
            obj.results_set.set(Results.objects.filter(
                product__category=obj.category))
        return obj


class ProductCategoryListView(mixins.ListModelMixin,
                              GenericViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductResultsListView(mixins.ListModelMixin,
                             GenericViewSet):
    queryset = Results.objects.all()
    serializer_class = ProductResultSerializer
    filterset_fields = ["product_id"]
