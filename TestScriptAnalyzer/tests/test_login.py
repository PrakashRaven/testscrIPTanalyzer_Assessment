import pytest
from playwright.sync_api import Page

@pytest.mark.smoke
def test_add_todo_and_verify(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc")
    page.locator("input.new-todo").fill("Buy milk")
    page.locator("input.new-todo").press("Enter")
    items = page.locator("ul.todo-list li")
    assert items.count() == 1
    assert items.nth(0).inner_text().strip() == "Buy milk"
