from django.db import models
from django.utils import timezone
from core.models import TimeStampModel, SoftDeleteModel


class Purchase(TimeStampModel, SoftDeleteModel):
    STATUS_CHOICES = (
        ('PAYMENT_REQUEST', 'PAYMENT_REQUEST'),  # 결제요청
        ('PAYMENT_COMPLETE', 'PAYMENT_COMPLETE'),  # 결제완료
        ('PAYMENT_FAILED', 'PAYMENT_FAILED'),  # 결제실패
        ('REFUND_REQUEST', 'REFUND_REQUEST'),  # 환불 요청
        ('REFUND_COMPLETE', 'REFUND_COMPLETE'),  # 환불 처리 완료
        ('REFUND_REJECT', 'REFUND_REJECT'),  # 환불 처리 반려
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        related_name='purchases'
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        related_name='purchases'
    )
    status = models.CharField('결제 상태', max_length=50, choices=STATUS_CHOICES, default='PAYMENT_REQUEST')
    amount = models.DecimalField('구매 시 금액', default=0, max_digits=10, decimal_places=2)

    completed_at = models.DateTimeField('결제 완료 날짜', null=True, default=None)
    refund_request_at = models.DateTimeField('환불 요청 날짜', null=True, default=None)
    refund_completed_at = models.DateTimeField('환불 처리 날짜', null=True, default=None)

    class Meta:
        db_table = 'purchases'
        ordering = ['-id']
        indexes = []

    def __str__(self):
        return f'{self.id}'

    def payment_complete(self):
        self.status = 'PAYMENT_COMPLETE'
        self.completed_at = timezone.now()
        self.save()

    def refund_request(self):
        self.status = 'REFUND'
        self.refund_request_at = timezone.now()
        self.save()

    def refund_complete(self):
        self.status = 'REFUND_COMPLETE'
        self.refund_completed_at = timezone.now()
        self.save()

    def refund_reject(self):
        self.status = 'REFUND_REJECT'
        self.refund_completed_at = timezone.now()
        self.save()
