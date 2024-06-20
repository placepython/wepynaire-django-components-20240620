from django.db import models

from django_extensions.db.fields import AutoSlugField


class WePynaireManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)


class WePynaire(models.Model):
    title = models.CharField("wepynaire title", max_length=255)
    slug = AutoSlugField(populate_from=["title"], editable=True)
    start_datetime = models.DateTimeField(
        "wepynaire start datetime", blank=True
    )
    duration = models.DecimalField(
        "wepynaire duration",
        max_digits=2,
        decimal_places=1,
        blank=True,
        null=True,
    )

    objects = WePynaireManager()

    class Meta:
        verbose_name = "wepynaire"
        verbose_name_plural = "wepynaires"

    def __str__(self):
        return self.title

    def natural_key(self):
        return (self.slug,)
