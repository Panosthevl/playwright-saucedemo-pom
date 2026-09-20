from pages.BasePage import Basepage

class CheckoutOverviewPage(Basepage):
    def __init__(self, page):
        super().__init__(page)
        
        self.subtotal_label = page.locator(".summary_subtotal_label")
        self.tax_label = page.locator(".summary_tax_label")
        self.total_label = page.locator(".summary_total_label")
        self.finish_button = page.locator("#finish")

    def finish_click(self):
        self.finish_button.click()
