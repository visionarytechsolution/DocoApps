from django.db import models

from . import BaseModel, MetricUnit


# TODO: Probably of no use
class PackageDimension(BaseModel):
    dimension_unit = models.ForeignKey(MetricUnit, null=False, to_field='code', on_delete=models.CASCADE,
                                       limit_choices_to={'category': 'dimension'}, related_name='dimension_unit')
    length = models.PositiveIntegerField(null=False, default=1)
    width = models.PositiveIntegerField(null=False, default=1)
    height = models.PositiveIntegerField(null=False, default=1)

    weight_unit = models.ForeignKey(MetricUnit, null=False, to_field='code', on_delete=models.CASCADE,
                                    limit_choices_to={'category': 'weight'}, related_name='weight_unit')
    weight = models.PositiveIntegerField(null=False, default=1)

    def __str__(self):
        return f'{self.dimension_unit} - {self.weight_unit}'
