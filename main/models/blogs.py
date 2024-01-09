from django.db import models
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='pics', verbose_name=_('Image'))
    youtube_link = models.URLField(blank=True, null=True, verbose_name=_('You Tube link'))

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return f"{self.title}"
