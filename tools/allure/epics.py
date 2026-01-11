from enum import Enum

#Epic — это крупная часть продукта, объединяющая функциональные блоки, которые решают крупные задачи системы.
# Это уровень самого высокого абстрактного представления

class AllureEpic(str,Enum):
    LMS = "LMS system"
    STUDENT = "Student system"
    ADMINISTRATION = "Administration system"