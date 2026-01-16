from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active:bool = True

user_data = {
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
}

invalid_user_data = {
    "id": "one",
    "name": 1,
    "email": 1,
}

user = User(**user_data)
print(user)
print(user.is_active)


try:
    invalid_user = User(**invalid_user_data)
except Exception as e:
    print("Ошибка валидации", e)
