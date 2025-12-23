from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def take_screenshot(self, step_name):
        screenshot_path = f"reports/screenshots/{step_name}.png"
        self.page.screenshot(path=screenshot_path)