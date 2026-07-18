from services.food_api import get_product_by_barcode

def test_invalid_barcode_returns_none():
    product = get_product_by_barcode("0000000000000")
    assert product is None