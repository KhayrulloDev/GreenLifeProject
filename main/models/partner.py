from django.db import models
from django.utils.translation import gettext_lazy as _


class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    image = models.ImageField(upload_to='pics', verbose_name=_('Image'))
    country = models.CharField(max_length=255, verbose_name=_('Country'))

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')

    def __str__(self):
        return f"{self.name}"
