import pytest
from playwright.sync_api import Page

def _common_steps(page: Page):
    page.goto("https://demo.playwright.dev/todomvc")
    page.locator("input.new-todo").fill("Profile step")
    page.locator("input.new-todo").press("Enter")

@pytest.mark.regression
def test_profile_flow_a(page: Page) -> None:
    _common_steps(page)
    page.goto("https://demo.playwright.dev/todomvc")
    page.locator("input.new-todo").fill("Profile step")
    page.locator("input.new-todo").press("Enter")
    assert page.locator("ul.todo-list li").count() >= 1

@pytest.mark.regression
def test_profile_flow_b(page: Page) -> None:
    try:
        _common_steps(page)
        page.goto("https://demo.playwright.dev/todomvc")
        page.locator("input.new-todo").fill("Profile step")
        page.locator("input.new-todo").press("Enter")
        assert page.locator("ul.todo-list li").count() >= 1
    except Exception:
        pytest.fail("Unexpected error")
