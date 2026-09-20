from pages.BasePage import Basepage

class LoginPage(Basepage):
    def __init__(self,page):
        super().__init__(page)

        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login = page.locator("#login-button")
        self.error_locator = page.locator("[data-test='error']")

    def username_fill(self,text_to_send):
        self.username.fill(text_to_send)

    def password_fill(self,text_to_send):
        self.password.fill(text_to_send)

    def login_click(self):
        self.login.click()
