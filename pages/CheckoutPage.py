from pages.BasePage import Basepage

class Checkoutpage(Basepage):
    def __init__(self,page):
        super().__init__(page)
        self.checkout = page.locator("#checkout")
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.zip_code = page.get_by_placeholder("Zip/Postal Code")
        self.conti = page.locator("#continue")

    def fill_info(self,first,last,zip):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.zip_code.fill(zip)

    def continue_click(self):
        self.conti.click()