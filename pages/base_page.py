from playwright.sync_api import Page


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until="networkidle")
        # Используем networkidle для того, чтобы дождаться завершения загрузки всех сетевых запросов перед выполнением последующих шагов.
        # networkidle имеет смысл только в проектах без фоновых соединений или с заблокированными шумными запросами

    def reload(self):
        self.page.reload(
            wait_until="domcontentloaded")  # используется domcontentloaded для того, чтобы дождаться, когда DOM страницы будет полностью загружен
