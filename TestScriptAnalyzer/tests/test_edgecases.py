import pytest
from playwright.sync_api import Page

def test_no_assert_example(page: Page):
    page.goto("https://demo.playwright.dev/todomvc")
    page.locator("input.new-todo").fill("Edge case")
    page.locator("input.new-todo").press("Enter")
