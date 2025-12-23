# Behave
# Selenium BDD Automation Framework with Behave

This repository contains a Behavior-Driven Development (BDD) test automation framework using **Python**, **Behave** (a Cucumber-like BDD framework for Python), and **Selenium WebDriver** for browser automation.

The framework supports writing readable feature files in Gherkin syntax, implementing steps in Python, and executing tests across multiple browsers (locally).

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

Supported browsers:
- Chrome
- Firefox
- Edge

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   Use `requirements.txt` file with the following content (or install directly):
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
behve/
├── features/
│   ├── environment.py      # Hooks for setup/teardown (browser initialization)
│   ├── steps/              # Step definitions in Python
│   │   └── *.py
│   └── *.feature           # Gherkin feature files
├── requirements.txt
└── README.md
```

## Configuration

Browser selection is controlled via command-line options in `environment.py` .

Example setup in `features/environment.py`:
```python
from playwright.sync_api import sync_playwright

def before_all(context):
    """Launch browser based on -D browser=<name> (chrome|firefox|webkit)."""
    browser_name = context.config.userdata.get("browser", "chromium").lower()  # Default chromium
    context.playwright = sync_playwright().start()

    launch_options = {
        "headless": False,
        "slow_mo": 1000,
    }
    if browser_name == "chromium" or browser_name == "chrome":
        context.browser = context.playwright.chromium.launch(**launch_options)
    elif browser_name == "firefox":
        context.browser = context.playwright.firefox.launch(**launch_options)
    elif browser_name == "webkit":
        context.browser = context.playwright.webkit.launch(**launch_options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}. Use: chrome, firefox, webkit")
    

def before_scenario(context, scenario):
    """Set up a new browser page before each scenario."""
    context.page = context.browser.new_page()
    context.page.set_viewport_size({"width": 1920, "height": 1080})


def after_all(context):
    """Close the browser and stop Playwright after all tests."""
    try:
        if context.browser:
            context.browser.close()
        if context.playwright:
            context.playwright.stop()
    except Exception as e:
        print(f"Error closing browser: {e}")
```

## Running Tests

### Run all tests on default browser (Chrome)
```bash
behave
```

### Run tests on a specific browser
Use the `-D` flag to pass userdata:
```bash
behave -D browser=chrome
behave -D browser=firefox
behave -D browser=edge
```

### Run tests on all supported browsers sequentially
You can chain commands in a script or manually:
```bash
behave utilities/run_all_browsers.py /features (to run all tests)
behave utilities/run_all_browsers.py /features/login.feature (to run a particular)
```

For parallel execution across browsers, consider integrating with tools like `pytest-bdd` or cloud platforms (e.g., BrowserStack, LambdaTest, Sauce Labs) by modifying `environment.py` to use remote WebDriver.

### Run specific features or scenarios
Use tags (add `@tag` to scenarios in `.feature` files):
```bash
behave -t @smoke / behave --tags=smoke
behave features/login.feature
```

### Generate allure reports
Behave supports formatted output:
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
behave serve reports/allure-results  # Generates report to a temp directory and start a web server
```

For HTML reports, install `behave-html-formatter`:
```bash
pip install behave-html-formatter
behave --format html --out reports/report.html
```

## Example Feature File

`features/example.feature`:
```gherkin
Feature: User Login

  Scenario: Verify user login
    Given I am on the login page
    When I filled the credentials
    And I clicked on login
    Then Verify logged success
```

Corresponding steps would be implemented in `features/steps/`.

## Contributing

Feel free to open issues or submit pull requests for improvements, new features, or bug fixes.

