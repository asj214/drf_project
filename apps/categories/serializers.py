from rest_framework import serializers
from core.serializers import RecursiveField
from .models import Category


class CategoryRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'parent_id',
            'name',
            'path',
            'depth',
            'order',
            'created_at',
            'updated_at',
        )


class CategorySerializer(serializers.ModelSerializer):
    parent_id = serializers.IntegerField(default=None, allow_null=True)
    name = serializers.CharField(max_length=256)
    order = serializers.IntegerField(default=1)
    depth = serializers.IntegerField(min_value=1, max_value=2)
    children = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'parent_id',
            'name',
            'path',
            'depth',
            'order',
            'created_at',
            'updated_at',
            'children',
        )

    def create(self, validated_data):
        user = self.context.get('user', None)
        category = Category.objects.create(
            user=user,
            **validated_data
        )

        category.set_path()

        return category

    def update(self, instance, validated_data):
        user = self.context.get('user', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.user = user
        instance.save()

        instance.set_path()

        return instance
