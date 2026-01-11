from enum import Enum


# Feature — это функциональная возможность продукта, более конкретная, чем epic, но всё ещё широкого охвата.
# Feature описывает отдельные аспекты системы, такие как конкретные модули или крупные функции

class AllureFeature(str, Enum):
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    AUTHENTICATION = "Authentication"
