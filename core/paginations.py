from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'per_page'

    def get_paginated_response(self, data):

        return Response({
            'prev': self.get_previous_link(),
            'next': self.get_next_link(),
            'count': self.page.paginator.count,
            'results': data
        })
