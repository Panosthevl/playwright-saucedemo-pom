# Playwright & Pytest QA Automation Framework (SauceDemo)

![Build Status](https://github.com)
![Python](https://shields.io)
![Playwright](https://shields.io🎭-green?style=for-the-badge)
![Pytest](https://shields.io)

A production-ready, enterprise-level UI Automation Framework built from scratch using **Python**, **Playwright**, and **Pytest**. This framework models and validates the standard e-commerce workflows of the SauceDemo platform using industry-standard QA architecture.
##  Contact & Connect
* **Developer:** Panagiotis Vlaras
* **LinkedIn:** [:panagiotis-vlaras](https://www.linkedin.com/in/panagiotis-vlaras)
* **GitHub Profile:** [@Panosthevl](https://github.com/Panosthevl/playwright-saucedemo-pom)

## Key Framework Features

* **Advanced Page Object Model (POM):** Complete separation of UI selectors and actions from test scripts using object-oriented principles and clean base class inheritance.
* **Indirect Parametrization & Dynamic Fixtures:** Optimized user authentication pipelines in `conftest.py` allowing multi-user data-driven testing without code duplication.
* **Business Logic & Tax Validation:** Deep data manipulation using string parsing, float conversion, and precision math for shopping cart checkout and dynamic tax verification.
* **Parametric UI Filtering & Sorting:** Dynamic list tracking validating automated ascending/descending product sorting logic (Low-to-High / High-to-Low).
* **Advanced HTML Reporting with Live Screenshots:** Custom Pytest hook implementation that generates visual diagnostic HTML reports with dynamic status charts and automatically embeds target failure/xfail window screenshots.
* **CI/CD Cloud Infrastructure:** Fully integrated with GitHub Actions workflows running automated parallel test executions headless on cloud-provisioned Linux instances.
* **Configuration & Secret Management:** Protected system architecture isolating critical URLs and environment credentials inside dynamic `.env` files.

## 📁 Project Architecture

```text
saucedemo/
├── .github/workflows/      # CI/CD Cloud Automation Workflows
├── pages/                  # Page Object Model Layer (UI Components & Logic)
│   ├── __init__.py
│   ├── BasePage.py
│   ├── CheckoutOverview.py
│   ├── InventoryPage.py
│   └── loginpage.py
├── tests/                  # Functional Testing Layer (Pytest Test Cases)
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_bug_cart.py
│   ├── test_cart.py
│   ├── test_checkout_overview.py
│   ├── test_login.py
│   └── test_sort.py
├── conftest.py             # Centralized Global Fixtures & Custom Reporting Hooks
├── pytest.ini              # Framework Constants & Automated Reporting Flags
├── .gitignore              # Secure Environment Tracking Exclusions
├── requirements.txt        # Project Dependencies & Packages
└── .env                    # Protected Environment Secrets & Credentials
```

## 💻 Local Installation & Execution

Follow these steps to set up and run the automation suite locally:

1. **Clone the repository and navigate to the project root:**
   ```bash
   git clone https://github.com
   cd playwright-saucedemo-pom
   ```

2. **Initialize and activate a Python virtual environment (`venv`):**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install project dependencies and browser binaries:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

4. **Run the automated test suite:**
   ```bash
   # Run all tests
   pytest

   # Run and generate the advanced HTML report
   pytest --html=report.html --self-contained-html
   ```
