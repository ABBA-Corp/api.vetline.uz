from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from .models import Product, ProductCategory, Results
from .serializers import (
    ProductListSerializer, ProductDetailSerializer,
    ProductCategorySerializer, ProductResultSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    """
    Поддерживаемые дополнительные параметры для изображений
    height: указывайте размер в пикселях для изображений
    width: указывайте размер в пикселях для изображений
    format: PNG, JPEG для того чтобы конвертировать изображения
    """
    queryset = Product.objects.select_related("category")
    list_serializer_class = ProductListSerializer
    serializer_class = ProductDetailSerializer
    filterset_fields = ["category_id", "is_top"]
    http_method_names = ["get"]

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class
        return self.serializer_class


class ProductCategoryListView(mixins.ListModelMixin,
                              GenericViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductBannerListView(mixins.ListModelMixin,
                            GenericViewSet):
    queryset = Results.objects.all()
    serializer_class = ProductResultSerializer