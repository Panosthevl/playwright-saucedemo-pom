#  Playwright & Pytest QA Automation Framework (SauceDemo)

[![Playwright UI Automation Tests Suite](https://github.com/Panosthevl)](https://github.com/Panosthevl)

A production-ready, enterprise-level UI Automation Framework built from scratch using **Python**, **Playwright**, and **Pytest**. This framework models the standard workflows of the SauceDemo e-commerce website using advanced architecture.

##  Key Framework Features
* **Advanced Page Object Model (POM):** Complete separation of UI selectors and actions from test scripts using object-oriented principles and clean base class inheritance.
* **Indirect Parametrization & Dynamic Fixtures:** Optimized user authentication pipelines in `conftest.py` allowing multi-user data-driven testing without code duplication.
* **Business Logic & Tax Validation:** Deep data manipulation using string parsing, float conversion, and precision math for shopping cart checkout and dynamic tax verification.
* **Parametric UI Filtering & Sorting:** Dynamic list tracking validating automated ascending/descending product sorting logic (Low-to-High / High-to-Low).
* **Advanced HTML Reporting with Live Screenshots:** Custom Pytest hook implementation that generates visual diagnostic HTML reports with dynamic status charts and automatically embeds target failure/xfail window screenshots.
* **CI/CD Cloud Infrastructure:** Fully integrated with GitHub Actions workflows running automated parallel test executions headless on cloud-provisioned Linux instances.
* **Configuration & Secret Management:** Protected system architecture isolating critical URLs and environment credentials inside dynamic `.env` files.

##  Project Architecture
```text
saucedemo/
├── .github/workflows/   # CI/CD Cloud Automation Configuration
├── pages/               # Page Object Model Layer (UI Components & Logic)
        __init__py
        BasePage.py
        CheckoutOverview.py
        InventoryPage.py
        loginpage.py

├── tests/               # Functional Testing Layer (Pytest Test Cases)
        __init__.py
        test_api.py
        test_bug_cart.py
        test_cart.py
        test_checkout_overview.py
        test_login.py
        test_sort.py
├── conftest.py          # Centralized Global Fixtures, Environments & Reporting Hooks
├── pytest.ini           # Framework Constants & Automated Reporting Flags
├── .gitignore           # Secure Environment Tracking Exclusions
└── .env                 # Protected Environment Secrets & Credentials
```

## Local Installation & Execution
1. Clone the repository and navigate into the workspace.
2. Initialize and activate a Python virtual environment (`venv`).
3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   pip install pytest-html python-dotenv pytest-playwright
   ```
4. Run the automated test suite execution:
   ```bash
   pytest
   ```
