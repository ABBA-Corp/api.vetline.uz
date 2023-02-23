from django.contrib import admin

from .models import Faqs


@admin.register(Faqs)
class FaqsAdmin(admin.ModelAdmin):
    list_display = ['faq_uz', 'answer_uz']
