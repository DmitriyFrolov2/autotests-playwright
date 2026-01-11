from enum import Enum


# Story — это конкретный пользовательский сценарий или задача, описывающая конкретные действия, которые может совершать пользователь или система.
# Story является самой детализированной аннотацией, используемой для описания автотестов.

class AllureStory(str, Enum):
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"
