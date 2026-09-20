import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize("logged_in",["problem_user"],indirect=True)
@pytest.mark.xfail(reason="Known bug for problem_user")
def test_bug_cart_badge(logged_in):
    inve = logged_in
    inve.add_product("sauce-labs-backpack")
    expect(inve.cart_icon).to_have_text("1")

    inve.page.locator("#remove-sauce-labs-backpack").click()

    expect(inve.cart_icon).to_have_text("")


