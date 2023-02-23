from django.contrib import admin

from .models import Product, ProductCategory, Results


class ResultsInline(admin.TabularInline):
    model = Results


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name_uz", "subtitle_uz", "is_top", "category"]
    inlines = [ResultsInline]
    list_editable = ['is_top']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["title_uz"]


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ["thumbnail_preview", "product", "title_uz", "subtitle_uz"]

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Фото'
    thumbnail_preview.allow_tags = True
