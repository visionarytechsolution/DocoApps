from functools import lru_cache

from django.db import models


class StateManager(models.Manager):

    @lru_cache(maxsize=10)
    def get_code_for_name(self, name):
        state = super().get_queryset().filter(name__iexact=name.strip()).first()
        return state.code if state else ''

    @lru_cache(maxsize=10)
    def get_obj_from_code(self, code):
        return super().get_queryset().filter(code__iexact=code).first()


class State(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    code = models.CharField(max_length=3, unique=True, null=False)

    objects = StateManager()

    class Meta:
        indexes = [
            models.Index(fields=['name', 'code'])
        ]

    def __str__(self):
        return f'{self.name}'
