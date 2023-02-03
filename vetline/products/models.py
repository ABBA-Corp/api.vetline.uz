from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from ordered_model.models import OrderedModel
from sorl.thumbnail import get_thumbnail, ImageField

from vetline.products.instances import get_shots_path, get_results_path


class Product(OrderedModel):
    name_uz = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    subtitle_uz = models.CharField(max_length=200)
    subtitle_en = models.CharField(max_length=200, null=True, blank=True)
    subtitle_ru = models.CharField(max_length=200, null=True, blank=True)
    photo = ImageField(_("Изображение"), upload_to=get_shots_path)
    category = models.ForeignKey("ProductCategory", on_delete=models.CASCADE,
                                 verbose_name=_("Категория продукта"))
    description_uz = models.TextField(_("Описание uz"))
    description_en = models.TextField(_("Описание en"), null=True, blank=True)
    description_ru = models.TextField(_("Описание ru"), null=True, blank=True)
    is_top = models.BooleanField(_("На топе?"), default=False)

    class Meta:
        verbose_name = _("Продукт")
        verbose_name_plural = _("Продукты")
        order_with_respect_to = "category"

    def __str__(self):
        return "{} | Категория: {}".format(self.name_uz, self.category.title_uz)

    @property
    def thumbnail_preview(self):
        if self.photo:
            _thumbnail = get_thumbnail(self.photo, '150x150', upscale=False, crop="center", quality=100)
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""


class ProductCategory(models.Model):
    title_uz = models.CharField(_('Заголовок uz'), max_length=100)
    title_en = models.CharField(_('Заголовок en'), max_length=100, null=True, blank=True)
    title_ru = models.CharField(_('Заголовок ru'), max_length=100, null=True, blank=True)
    photo = ImageField(_('Фото'))

    class Meta:
        verbose_name = _('Категория товара')
        verbose_name_plural = _('Категории товаров')

    def __str__(self):
        return "%s" % self.title_uz


class Results(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('Продукт'), on_delete=models.CASCADE)
    photo = ImageField(_("Изображение"), upload_to=get_results_path)
    title = models.CharField(_("Заголовок"), max_length=255)
    subtitle = models.CharField(_("Подзаголовок"), max_length=255)

    class Meta:
        verbose_name = _("Результат")
        verbose_name_plural = _("Результаты")

    @property
    def thumbnail_preview(self):
        if self.photo:
            _thumbnail = get_thumbnail(self.photo, '350x200', upscale=False, crop="center", quality=100)
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""
