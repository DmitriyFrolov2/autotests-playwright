from playwright.sync_api import Page, expect
from typing import Pattern
import allure

from tools.logger import get_logger

logger = get_logger("BASE_PAGE")

class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f'Открываем url "{url}"'

        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="networkidle")
            # Используем networkidle для того, чтобы дождаться завершения загрузки всех сетевых запросов перед выполнением последующих шагов.
            # networkidle имеет смысл только в проектах без фоновых соединений или с заблокированными шумными запросами

    def reload(self):
        step = f'Перезагружаем страницу с адресом "{self.page.url}"'

        with allure.step(step):
            logger.info(step)
            self.page.reload(
                wait_until="domcontentloaded")  # используется domcontentloaded для того, чтобы дождаться, когда DOM страницы будет полностью загружен

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Проверяем, что текущий url соответствует шаблону "{expected_url.pattern}"'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
