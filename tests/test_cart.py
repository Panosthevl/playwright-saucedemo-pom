from pages.InventoryPage import Inventorypage
from playwright.sync_api import expect
import pytest
def test_cart(logged_in):
    logged_in.add_product("sauce-labs-backpack")
    logged_in.add_product("sauce-labs-bike-light")

    expect(logged_in.cart_icon).to_have_text("2")
