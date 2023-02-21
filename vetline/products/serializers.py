from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from .models import Product, ProductCategory, Results


class ThumbnailSerializer(serializers.Serializer):
    thumbnail = HyperlinkedSorlImageField(
        '500x500',
        options={"format": "PNG"},
        source='photo',
        read_only=True
    )


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductListSerializer(ThumbnailSerializer, serializers.ModelSerializer):  # noqa

    class Meta:
        model = Product
        fields = "__all__"


class ProductResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = "__all__"


class ProductDetailSerializer(ThumbnailSerializer, serializers.ModelSerializer):  # noqa
    results_set = ProductResultSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        x = super().to_representation(instance)
        if not x['results_set']:
            x['results_set'] = Results.objects.filter(
                product__category=instance.category).values()
        return x
