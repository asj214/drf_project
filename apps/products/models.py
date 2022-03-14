from django.db import models
from core.models import TimeStampModel, SoftDeleteModel


class Product(TimeStampModel, SoftDeleteModel):
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        related_name='products'
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        related_name='products'
    )
    name = models.CharField('상품명', max_length=255)
    amount = models.DecimalField('상품금액', default=0, max_digits=10, decimal_places=2)
    description = models.TextField('상품설명', null=True, default=None, blank=True)

    class Meta:
        db_table = 'products'
        ordering = ['-id']
        indexes = []

    def __str__(self):
        return f'{self.id}'
