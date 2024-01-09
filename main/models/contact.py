from django.db import models
from main.models.product import Product
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    phone_number = models.CharField(max_length=13, verbose_name=_('Phone Number'))
    email = models.EmailField(max_length=255, verbose_name=_('Email'))
    message = models.TextField(verbose_name=_('Message'))

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return f"{self.name}"
