import os
from pathlib import Path
from dotenv import load_dotenv 

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)


import pytest
from pages.loginpage import LoginPage 
from pages.InventoryPage import Inventorypage
from pages.CheckoutPage import Checkoutpage
from pages.CheckoutOverviewPage import CheckoutOverviewPage

@pytest.fixture(scope="function")
def login_page(page):

    return LoginPage(page)


@pytest.fixture(scope="function")
def logged_in(page,login_page,request):
    logged_page = Inventorypage(page)
    username = getattr(request,"param","standard_user")
    logged_page.navigate()
    login_page.username_fill(username)
    login_page.password_fill(os.getenv("password"))
    login_page.login_click()

    return logged_page



@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield 
    if hasattr(request.node, "rep_call"):
        
        failed = request.node.rep_call.failed
        
        xfail = hasattr(request.node, "rep_setup") and hasattr(request.node.rep_call, "wasxfail")
        
        
        if failed or xfail:
            test_name = request.node.name
            try:
                page.screenshot(path=f"bug_{test_name}.png", full_page=True)
                print(f"\n📸 The screenshot is saved for the test bug or xfail  {test_name}")
            except Exception:
                pass

@pytest.fixture(scope="function")
def checkout_page(page):
    return Checkoutpage(page)

@pytest.fixture(scope="function")
def logged_in_checkout_overview(page,logged_in,checkout_page):
    logged_in.add_product("sauce-labs-backpack")
    logged_in.add_product("sauce-labs-bike-light")

    logged_in.cart_icon.click()
    checkout_page.checkout.click()
    checkout_page.fill_info("Panos","Vlaras","47100")
    checkout_page.continue_click()

    return CheckoutOverviewPage(page)

