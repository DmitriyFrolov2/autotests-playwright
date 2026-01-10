from playwright.sync_api import Page, Locator, expect


# Этот класс описывает общие методы и логику для работы с любыми элементами на странице
# Это решение позволяет разделить интерфейсы в зависимости от типов элементов, что делает код более чистым и логически структурированным.
class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    # Метод принимает кейворд аргументы (kwargs)
    def get_locator(self, nht: int = 0, **kwargs) -> Locator:  # объект Locator для взаимодействия с элементом
        # Инициализирует объект локатора, подставляя динамические значения в локатор.
        locator = self.locator.format(**kwargs)
        # Возвращаем объект локатора
        return self.page.get_by_test_id(locator).nth(nht)

    def click(self, nht: int = 0, **kwargs):
        # "Лениво" инициализируем локатор
        locator = self.get_locator(nht, **kwargs)
        # Выполняем нажатие на элемент
        locator.click()

    def check_visible(self, nht: int = 0, **kwargs):
        # Инициализируем локатор "лениво"
        locator = self.get_locator(nht, **kwargs)
        # Проверяем, что элемент виден на странице
        expect(locator).to_be_visible()

    def check_have_text(self,  text: str, nht: int = 0, **kwargs):
        locator = self.get_locator(nht, **kwargs)
        expect(locator).to_have_text(text)
