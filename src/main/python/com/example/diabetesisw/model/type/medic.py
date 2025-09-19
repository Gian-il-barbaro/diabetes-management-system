from typing import List, Dict, Any
import sqlite3
from .general_type import GeneralType

class Medic(GeneralType):
    STRING_ID = "medic_id"

    def __init__(self, name: str = "", surname: str = "", email: str = "", password: str = "", medic_id: int = -1):
        self._medic_id = medic_id
        self._name = name
        self._surname = surname
        self._email = email.lower() if email else ""
        self._password = password

    @classmethod
    def from_constructor(cls, name: str, surname: str, email: str, password: str) -> 'Medic':
        return cls(name, surname, email, password)

    @classmethod
    def from_db(cls, medic_id: int, name: str, surname: str, email: str, password: str) -> 'Medic':
        return cls(name, surname, email, password, medic_id)

    @staticmethod
    def getFromResultSet(row: sqlite3.Row) -> 'Medic':
        return Medic.from_db(
            row["medic_id"],
            row["name"],
            row["surname"],
            row["email"],
            row["password"]
        )

    def medicIdProperty(self) -> int:
        return self._medic_id

    def getName(self) -> str:
        return self._name

    def setName(self, name: str) -> None:
        self._name = name

    def nameProperty(self) -> str:
        return self._name

    def getSurname(self) -> str:
        return self._surname

    def setSurname(self, surname: str) -> None:
        self._surname = surname

    def surnameProperty(self) -> str:
        return self._surname

    def getEmail(self) -> str:
        return self._email

    def setEmail(self, email: str) -> None:
        self._email = email.lower()

    def emailProperty(self) -> str:
        return self._email

    def getPassword(self) -> str:
        return self._password

    def setPassword(self, password: str) -> None:
        self._password = password

    def passwordProperty(self) -> str:
        return self._password

    def copyWithDiffId(self, id: int) -> 'Medic':
        return Medic.from_db(id, self._name, self._surname, self._email, self._password)

    def getId(self) -> int:
        return self._medic_id

    def getStringId(self) -> str:
        return self.STRING_ID

    def getProperties(self) -> List[Any]:
        return [
            self._name,
            self._surname,
            self._email,
            self._password
        ]

    def getPropertiesType(self) -> Dict[Any, str]:
        return {
            self._name: str.__name__,
            self._surname: str.__name__,
            self._email: str.__name__,
            self._password: str.__name__
        }