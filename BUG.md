# BUG: Cart badge stays at '1' after clicking Remove (problem_user) and the button state doesnt change.

##  Details
- **Test Website:** SauceDemo (https://saucedemo.com)
- **Impact:** Medium (Annoying UI behavior for the user)
- **Found by:** Automated Test (`test_bug_cart.py`)
- **Status in Code:** Marked as `@pytest.mark.xfail`

---

## What is the issue?
When I log in with the `problem_user` account and add an item to the shopping cart, the badge correctly shows `1`. But if I change my mind and click the "Remove" button, the button doesnt resets to "Add to cart" and the red badge **still stays on the screen showing '1'**. 

---

## 🛠️ How to reproduce it
1. Go to `https://saucedemo.com`
2. Log in with user: `problem_user` / password: `secret_sauce`
3. Click **"Add to cart"** on the *Sauce Labs Backpack*. (Badge shows `1` - Correct)
4. Click the **"Remove"** button on the exact same product.

---

## What should happen (Expected)
The button state should change to "Add to Cart" and the red cart badge should vanish or drop to `0` because the cart is now empty.

## What actually happens (Actual)
The button text doesnt change, but the cart badge **is still stuck at '1'**.

---

##  QA Note
I verified this behavior using both manual testing and my Playwright automation script. The bug is isolated only to this specific user profile (`problem_user`).
