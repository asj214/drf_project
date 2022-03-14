from django.db import models
from core.models import TimeStampModel, SoftDeleteModel


class Category(TimeStampModel, SoftDeleteModel):
    parent = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        null=True,
        related_name='children'
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        related_name='categories'
    )
    name = models.CharField('카테고리명', max_length=256)
    path = models.JSONField('카테고리 경로', null=True, default=None)
    depth = models.IntegerField('뎁스', default=1)
    order = models.IntegerField('정렬순위', default=1)

    class Meta:
        db_table = 'categories'
        ordering = ['depth', 'order']
        indexes = []

    def __str__(self):
        return f'{self.name}'
    
    def make_path(self, path: list = []):
        path.append(self.name)
        if self.parent_id is None:
            return list(reversed(path))
        else:
            return self.parent.make_path(path)
    
    def set_path(self):
        self.path = self.make_path(path=[])
        self.save()