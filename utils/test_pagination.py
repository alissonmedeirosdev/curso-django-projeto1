from unittest import TestCase
from utils.pagination import make_pagination_range

class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1,21)), # Lista de números 
            qty_pages=4, # Quantidades de paginas exibidas
            current_page=1 # Pagina atual que o usuario está
        )['pagination']

        self.assertEqual([1,2,3,4], pagination)

    def test_first_range_is_static_if_current_page_is_less_then_middle_page(self):
        pagination = make_pagination_range(
            page_range=list(range(1,21)), 
            qty_pages=4, 
            current_page=1 
        )['pagination']

        self.assertEqual([1,2,3,4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1,21)), 
            qty_pages=4, 
            current_page=3
        )['pagination']

        self.assertEqual([2,3,4,5], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination = make_pagination_range(
            page_range=list(range(1,21)), 
            qty_pages=4, 
            current_page=20
        )['pagination']

        self.assertEqual([17,18,19,20], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1,21)), 
            qty_pages=4, 
            current_page=21
        )['pagination']

        self.assertEqual([17,18,19,20], pagination)

        