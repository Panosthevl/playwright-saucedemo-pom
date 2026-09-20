from pages.BasePage import Basepage
class Inventorypage(Basepage):
    def __init__(self,page):
        super().__init__(page)
        self.cart_icon= page.locator(".shopping_cart_link")
        self.dropdown= page.locator("[data-test='product-sort-container']")
        self.product_prices = page.locator(".inventory_item_price")
    def add_product(self,product_name):
        dynamic_selector = f"#add-to-cart-{product_name}"

        self.page.locator(dynamic_selector).click()

    def sort_products(self,option_value):
        """
        option_value: 'az' (A to Z), 'za' (Z to A), 'lohi' (Low to High), 'hilo' (High to Low)
        """
        self.dropdown.select_option(option_value)





