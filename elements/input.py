from playwright.sync_api import Locator, expect
import allure
from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("INPUT")

# Методы сппецифичные для полей ввода
class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Заполняем {self.type_of} "{self.name}" значением "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0,
                         **kwargs):  # метод, который проверяет значение, находящееся в поле ввода
        step = f'Проверяем, что в {self.type_of} "{self.name}" значение "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)
