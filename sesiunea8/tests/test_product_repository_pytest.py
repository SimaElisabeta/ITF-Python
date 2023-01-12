import pytest
from sesiunea8.app.product import Product
from sesiunea8.app.product_repository import ProductRepository


class TestProductRepository:
    def setup_method(self):
        self.repo = ProductRepository()

    def test_get_all(self):
        assert self.repo.get_all() == self.repo.products

    @pytest.mark.parametrize('name, expected', [
        ("Oua", Product(name="Oua", price=14.79, discount=5, category="Alimente de baza")),
        ("Ovaz", Product(name="Ovaz", price=1.99, discount=0, category="Alimente de baza")),
        ("Vin", None)
    ])
    def test_get_by_name(self, name, expected):
        assert self.repo.get_by_name(name) == expected

    @pytest.mark.parametrize('category, expected', [
        ('Fainoase', ['Paine neagra', 'Faina integrala']),
        ('Lactate', ['Branza de capra']),
        ('Dulciuri', [])
    ])
    def test_get_all_name_by_category(self, category, expected):
        assert self.repo.get_all_name_by_category(category) == expected
