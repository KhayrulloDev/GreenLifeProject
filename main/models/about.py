from django.db import models
from django.utils.translation import gettext_lazy as _


class About(models.Model):
    text = models.TextField(verbose_name=_('Text'), blank=True, null=True)

    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('Abouts')

    def __str__(self):
        return f"About"
