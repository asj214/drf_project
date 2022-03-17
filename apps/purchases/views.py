from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Purchase
from .serializers import PurchaseSerializer


class PurchaseListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.prefetch_related(
        'product__category'
    ).all()

    def get_queryset(self):
        filters = {
            'user_id': self.request.user.id
        }
        return self.queryset.filter(**filters)

    def get(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        purchases = request.data.get('purchases', [])
        length = len(purchases)
        if length == 0 or length > 30:
            raise ValidationError('MAX_LIMIT_OVER')

        serializer = self.serializer_class(
            data=purchases,
            context={'user': request.user},
            many=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
