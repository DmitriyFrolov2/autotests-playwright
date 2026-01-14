from playwright.sync_api import Page, expect
from typing import Pattern
import allure


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Открываем url "{url}"'):
            self.page.goto(url, wait_until="networkidle")
            # Используем networkidle для того, чтобы дождаться завершения загрузки всех сетевых запросов перед выполнением последующих шагов.
            # networkidle имеет смысл только в проектах без фоновых соединений или с заблокированными шумными запросами

    def reload(self):
        with allure.step(f'Перезагружаем страницу с адресом "{self.page.url}"'):
            self.page.reload(
                wait_until="domcontentloaded")  # используется domcontentloaded для того, чтобы дождаться, когда DOM страницы будет полностью загружен

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Проверяем, что текущий url соответствует шаблону "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)
