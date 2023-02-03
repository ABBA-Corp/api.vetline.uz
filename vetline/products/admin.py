from django.contrib import admin

from .models import Product, ProductCategory, Results


class ResultsInline(admin.TabularInline):
    model = Results


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name_uz", "subtitle_uz", "is_top"]
    inlines = [ResultsInline]
    list_editable = ['is_top']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["title_uz"]
