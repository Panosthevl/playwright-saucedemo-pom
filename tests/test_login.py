import pytest
from playwright.sync_api import expect 

@pytest.mark.parametrize("input_user", [
    "standard_user",
    "performance_glitch_user",
    "problem_user",
    "error_user",
    "visual_user"
])
def test_successful_users_login(login_page, input_user):
    login_page.navigate()
    login_page.username_fill(input_user)
    login_page.password_fill("secret_sauce")
    login_page.login_click()

    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_locked_out_user_error(login_page):
    login_page.navigate()
    login_page.username_fill("locked_out_user")
    login_page.password_fill("secret_sauce")
    login_page.login_click()
    
    expect(login_page.error_locator).to_be_visible()
    expect(login_page.error_locator).to_contain_text("Sorry, this user has been locked out.")

