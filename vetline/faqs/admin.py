from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from .models import Faqs


@admin.register(Faqs)
class FaqsAdmin(OrderedModelAdmin):
    list_display = ['faq_uz', 'answer_uz', 'move_up_down_links', 'order']
    ordering = ['order']
