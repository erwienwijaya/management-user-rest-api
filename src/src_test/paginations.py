from rest_framework import pagination
from rest_framework.response import Response

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 10

class CustomPagination(pagination.PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    # code pagination: limit & offset
    # default_limit = 10
    # limit_query_param = 'l'
    # offset_query_param = 'o'
    # max_limit = 50

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'metadata': {
                'total': self.page.paginator.count,
                'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
                'total_pages': self.page.paginator.num_pages,
                'page_size': int(self.request.GET.get('page_size', self.page_size))
            },
            'results': data
        })