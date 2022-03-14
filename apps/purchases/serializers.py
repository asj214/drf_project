from django.db import transaction
from rest_framework import serializers
from apps.products.models import Product
from apps.products.serializers import ProductRelatedSerializer
from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    product = ProductRelatedSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = (
            'id',
            'product',
            'product_id',
            'amount',
            'status',
            'completed_at',
            'refund_request_at',
            'refund_completed_at',
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        user = self.context.get('user', None)
        product_id = validated_data.get('product_id', None)
        has = user.purchases.filter(product_id=product_id).first()

        if has is not None:
            raise serializers.ValidationError('PRODUCT_EXISTS')

        with transaction.atomic():
            product = Product.objects.get(pk=product_id)
            purchase = user.purchases.create(
                product=product,
                amount=product.amount,
            )

            # 임시 결제 완료 처리
            purchase.payment_complete()

        return purchase
