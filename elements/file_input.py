from elements.base_element import BaseElement
import allure

class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "FileInput"

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        with allure.step(f'Загружаем файл "{file}" в {self.type_of} "{self.name}"'):
            locator = self.get_locator(nth,**kwargs)
            locator.set_input_files(file)