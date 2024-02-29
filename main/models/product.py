from django.db import models
from main.models.partner import Partner
from main.models.category import Category
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    price = models.CharField(max_length=20, verbose_name=_('Price'), blank=True, null=True)
    productivity = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Productivity'))
    organization = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Organization'))
    category = models.CharField(max_length=255, verbose_name=_('Category'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Partner ID'))
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category ID'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f"{self.name}"
