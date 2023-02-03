from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from .models import Product, ProductCategory, Results


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):  # noqa
    thumbnail_photo = serializers.SerializerMethodField()  # noqa

    class Meta:
        model = Product
        fields = "__all__"

    def get_thumbnail_photo(self, obj):
        height = self.context['request'].GET.get('height', '500')  # noqa
        width = self.context['request'].GET.get('width', '500')
        img_format = self.context['request'].GET.get('format', 'PNG')
        quality = self.context['request'].GET.get('quality', 50)
        thumbnail = get_thumbnail(obj.photo, f'{width}x{height}', quality=int(quality), format=img_format.upper())
        return {
            "size": thumbnail.size,
            "url": self.context['request'].build_absolute_uri(thumbnail.url),
        }


class ProductResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):  # noqa
    thumbnail_photo = serializers.SerializerMethodField()  # noqa
    results_set = ProductResultSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def get_thumbnail_photo(self, obj):
        height = self.context['request'].GET.get('height', '500')  # noqa
        width = self.context['request'].GET.get('width', '500')
        img_format = self.context['request'].GET.get('format', 'PNG')
        quality = self.context['request'].GET.get('quality', 50)
        thumbnail = get_thumbnail(obj.photo, f'{width}x{height}', quality=int(quality), format=img_format.upper())
        return {
            "size": thumbnail.size,
            "url": self.context['request'].build_absolute_uri(thumbnail.url),
        }
