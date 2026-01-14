from playwright.sync_api import expect
import allure
from elements.base_element import BaseElement

# Эти методы инкапсулируют проверки, которые выполняли вручную при работе с кнопками
class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Проверяем, что {self.type_of} "{self.name}" активна'):
            locator = self.get_locator(nth,**kwargs)
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Проверяем, что {self.type_of} "{self.name}" неактивна'):
            locator = self.get_locator(nth,**kwargs)
            expect(locator).to_be_disabled()