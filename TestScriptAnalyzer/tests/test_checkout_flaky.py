import time
import pytest
from playwright.sync_api import Page

@pytest.mark.flaky
def test_flaky_waits(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc")
    time.sleep(4)
    page.locator("input.new-todo").fill("Flaky item")
    page.locator("input.new-todo").press("Enter")
    time.sleep(2)
    assert page.locator("ul.todo-list li").count() >= 1
