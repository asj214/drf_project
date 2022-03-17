from rest_framework import serializers
from apps.categories.serializers import CategoryRelatedSerializer
from .models import Product


class ProductRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category_id',
            'name',
            'amount',
            'description',
            'created_at',
            'updated_at',
        )


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategoryRelatedSerializer(read_only=True)
    name = serializers.CharField(max_length=255)
    amount = serializers.DecimalField(default=0, max_digits=10, decimal_places=2)
    description = serializers.CharField()

    class Meta:
        model = Product
        fields = (
            'id',
            'category_id',
            'category',
            'name',
            'amount',
            'description',
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        user = self.context.get('user', None)
        return Product.objects.create(
            user=user,
            **validated_data
        )

    def update(self, instance, validated_data):
        user = self.context.get('user', None)
        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.user = user
        instance.save()

        return instance
