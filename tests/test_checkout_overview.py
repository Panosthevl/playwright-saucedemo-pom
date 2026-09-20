import pytest
def test_checkout_math(logged_in_checkout_overview):
    overview = logged_in_checkout_overview
    
    subtotal_text = overview.subtotal_label.inner_text()
    tax_text = overview.tax_label.inner_text()
    total_text = overview.total_label.inner_text()

    actual_subtotal = float(subtotal_text.split("$")[1])
    actual_tax = float(tax_text.split("$")[1])
    actual_total = float(total_text.split("$")[1])

    expected_tax= round(actual_subtotal*0.08,2)
    expected_total = round(actual_subtotal + expected_tax,2)

    assert actual_tax == expected_tax
    assert actual_total == expected_total