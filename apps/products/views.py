from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from core.permissions import StaffOrReadOnly
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [StaffOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.prefetch_related(
        'category__children'
    ).all()

    def get_queryset(self):
        return self.queryset

    def get_object(self, pk=None):
        try:
            return self.get_queryset().get(pk=pk)
        except Product.DoesNotExist:
            raise NotFound('Not Found')
    
    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'user': request.user}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        product = self.get_object(pk)
        serializer = self.serializer_class(product)

        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        product = self.get_object(pk)
        serializer = self.serializer_class(
            product,
            data=request.data,
            context={'user': request.user},
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
    def destroy(self, request, pk=None, *args, **kwargs):
        product = self.get_object(pk)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)