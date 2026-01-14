from playwright.sync_api import Locator, expect
import allure
from elements.base_element import BaseElement


# Методы сппецифичные для полей ввода
class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):  # метод, который заполняет поле ввода указанным текстом.
        with allure.step(f'Заполняем {self.type_of} "{self.name}" значением "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0,
                         **kwargs):  # метод, который проверяет значение, находящееся в поле ввода
        with allure.step(f'Проверяем, что в {self.type_of} "{self.name}" значение "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)
