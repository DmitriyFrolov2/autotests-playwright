from playwright.sync_api import Page, Locator, expect
import allure

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
        with allure.step(f'Получаем элемент с атрибутом data-testid="{locator}" с индексом {nth}'):
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        with allure.step(f'Кликаем по {self.type_of} "{self.name}"'):
            # "Лениво" инициализируем локатор
            locator = self.get_locator(nth, **kwargs)
            # Выполняем нажатие на элемент
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        with allure.step(f'Проверяем, что {self.type_of} "{self.name}" отображается на странице'):
            locator = self.get_locator(nth, **kwargs)
            # Проверяем, что элемент виден на странице
            expect(locator).to_be_visible()

    def check_have_text(self,  text: str, nth: int = 0, **kwargs):
        with allure.step(f'Проверяем, что у {self.type_of} "{self.name}" текст равен "{text}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(text)
