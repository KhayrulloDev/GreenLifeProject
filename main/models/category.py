from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(MPTTModel):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Name'))
    parent = TreeForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name=_('Parent'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return f"{self.name}"
