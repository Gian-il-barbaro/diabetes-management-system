from typing import List, TypeVar, Generic, Any, Optional
import json

T = TypeVar('T')

class StringListProperty(Generic[T]):
    def __init__(self, type_class: type, owner: Any, name: str):
        self._type_class = type_class
        self._owner = owner
        self._name = name
        self._items: List[T] = []
        self._string_value = "[]"

    def add(self, item: T) -> None:
        self._items.append(item)
        self._update_string_value()

    def addAll(self, items: List[T]) -> None:
        self._items.extend(items)
        self._update_string_value()

    def get(self) -> List[T]:
        return self._items.copy()

    def set(self, string_value: str) -> None:
        self._string_value = string_value
        try:
            parsed = json.loads(string_value) if string_value else []
            if self._type_class == int or self._type_class == Integer:
                self._items = [int(x) for x in parsed if isinstance(x, (int, str))]
            else:
                self._items = [str(x) for x in parsed]
        except (json.JSONDecodeError, ValueError):
            self._items = []

    def stringProperty(self) -> 'StringProperty':
        return StringProperty(self._owner, f"{self._name}_string", self._string_value)

    def _update_string_value(self) -> None:
        self._string_value = json.dumps(self._items)

class StringProperty:
    def __init__(self, owner: Any, name: str, initial_value: str = ""):
        self._owner = owner
        self._name = name
        self._value = initial_value

    def get(self) -> str:
        return self._value

    def set(self, value: str) -> None:
        self._value = value

class Integer:
    pass