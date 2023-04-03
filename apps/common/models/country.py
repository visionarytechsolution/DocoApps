from functools import lru_cache

from django.db import models


class CountryManager(models.Manager):

    @lru_cache(maxsize=10)
    def get_code_for_name(self, name):
        country = super().get_queryset().filter(name__iexact=name.strip()).first()
        return country.code if country else ''

    @lru_cache(maxsize=10)
    def get_obj_from_code(self, code):
        return super().get_queryset().filter(code__iexact=code).first()


class Country(models.Model):
    name = models.CharField(max_length=60, unique=True, null=False)
    code = models.CharField(max_length=2, unique=True, null=False)
    alpha_three_code = models.CharField(max_length=3, null=True)
    currency_code = models.CharField(max_length=3, unique=True, null=False)

    objects = CountryManager()

    class Meta:
        indexes = [
            models.Index(fields=['name', 'code'])
        ]
        verbose_name_plural = "countries"

    def __str__(self):
        return f'{self.name}'
