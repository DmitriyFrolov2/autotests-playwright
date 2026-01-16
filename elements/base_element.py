from playwright.sync_api import Page, Locator, expect
import allure
from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")

# Этот класс описывает общие методы и логику для работы с любыми элементами на странице
# Это решение позволяет разделить интерфейсы в зависимости от типов элементов, что делает код более чистым и логически структурированным.
class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:
        return "base element"

    # Метод принимает кейворд аргументы (kwargs)
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:  # объект Locator для взаимодействия с элементом
        # Инициализирует объект локатора, подставляя динамические значения в локатор.
        locator = self.locator.format(**kwargs)
        step = f'Получаем элемент с атрибутом data-testid="{locator}" с индексом {nth}'

        with allure.step(step):
            logger.info(step)
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        step = f'Кликаем по {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        step = f'Проверяем, что {self.type_of} "{self.name}" отображается на странице'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

    def check_have_text(self,  text: str, nth: int = 0, **kwargs):
        step = f'Проверяем, что у {self.type_of} "{self.name}" текст равен "{text}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)
