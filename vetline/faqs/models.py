from django.db import models
from django.utils.translation import gettext_lazy as _

from ordered_model.models import OrderedModel


class Faqs(OrderedModel):
    faq_uz = models.CharField(_("Вопрос uz"), max_length=500)
    faq_ru = models.CharField(_("Вопрос ru"), max_length=500, null=True, blank=True)
    faq_en = models.CharField(_("Вопрос en"), max_length=500, null=True, blank=True)
    answer_uz = models.CharField(_("Ответ uz"), max_length=500)
    answer_ru = models.CharField(_("Ответ ru"), max_length=500, null=True, blank=True)
    answer_en = models.CharField(_("Ответ en"), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")

    def __str__(self):
        return self.faq_uz
