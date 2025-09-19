from typing import Optional

class ModelOperators:
    _instance: Optional['ModelOperators'] = None
    DEFAULT_OPERATOR_EMAIL = "admin@diabetesystem.com"
    DEFAULT_OPERATOR_PASSWORD = "admin123"

    def __init__(self):
        pass

    @classmethod
    def getInstance(cls) -> 'ModelOperators':
        if cls._instance is None:
            cls._instance = ModelOperators()
        return cls._instance

    def isAuthorized(self, email: str, password: str) -> bool:
        return (email.lower() == self.DEFAULT_OPERATOR_EMAIL.lower() and
                password == self.DEFAULT_OPERATOR_PASSWORD)