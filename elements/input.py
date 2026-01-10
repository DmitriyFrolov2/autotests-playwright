from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement

# Методы сппецифичные для полей ввода
class Input(BaseElement):
    def get_locator(self, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator('input')

    def fill(self, value: str, **kwargs): # метод, который заполняет поле ввода указанным текстом.
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, **kwargs): # метод, который проверяет значение, находящееся в поле ввода
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)


