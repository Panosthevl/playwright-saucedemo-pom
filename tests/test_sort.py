import pytest
from pages.InventoryPage import Inventorypage
@pytest.mark.parametrize("sort_option",["lohi","hilo"])
def test_sort_by(logged_in,sort_option):
    inv = logged_in
    inv.sort_products(sort_option)
    html_prices = inv.product_prices.all_inner_texts()
    actual_prices = [float(price.split("$")[1]) for price in html_prices]

    if sort_option == "lohi":
        assert actual_prices == sorted(actual_prices),f"failed low to high! Found:{actual_prices}"

    elif sort_option == "hilo":
        assert actual_prices == sorted(actual_prices,reverse=True),f"Failed High to Low!Found:{actual_prices}"
