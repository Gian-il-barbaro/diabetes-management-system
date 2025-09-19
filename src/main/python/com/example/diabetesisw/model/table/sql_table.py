from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
import sqlite3
from ..type.general_type import GeneralType

T = TypeVar('T', bound=GeneralType)

class SQLTable(Generic[T], ABC):
    def __init__(self, table_type: str):
        from ..model import Model
        self.model = Model.getInstance()
        self.table_type = table_type
        self.table_name = table_type.lower()
        self.table_constructor = self._get_table_constructor()
        self.observable_list: List[T] = []

    def _get_table_constructor(self) -> str:
        from .tables_constructor import TablesConstructor
        return TablesConstructor.getTableConstructor(self.table_type)

    def getType(self) -> str:
        return self.table_type

    def getTableName(self) -> str:
        return self.table_name

    def getFromId(self, id: int) -> Optional[T]:
        for obj in self.observable_list:
            if obj.getId() == id:
                return obj
        return None

    def toList(self) -> List[T]:
        return self.observable_list.copy()

    def getObservableList(self) -> List[T]:
        return self.observable_list

    def getIdByIndex(self, index: int) -> int:
        return self.observable_list[index].getId()

    def exist(self) -> bool:
        return self.model.hasTable(self.table_name)

    def createTable(self) -> None:
        statement = f"CREATE TABLE {self.table_name} {self.table_constructor}"
        self.model.runStatement(statement)

    def dropTable(self) -> None:
        statement = f"DROP TABLE IF EXISTS {self.table_name};"
        self.model.runStatement(statement)

    def resetTable(self) -> None:
        self.dropTable()
        self.createTable()

    def load(self) -> None:
        result = self.model.query(f"SELECT * FROM {self.table_name}")

        for row in result:
            self.observable_list.append(self.getFromResultSet(row))

    def _addEntry(self, constructor: str, values: str) -> int:
        return self.model.insert(self.table_name, constructor, values)

    def insert(self, obj: T) -> T:
        if obj is None:
            raise RuntimeError("Error can't insert null object")

        try:
            entry_id = self._addEntry(obj.getTupleName(), obj.getTupleValues())
            created_entry = obj.copyWithDiffId(entry_id)
            self.observable_list.append(created_entry)
            return created_entry
        except Exception as e:
            raise RuntimeError(f"Failed to insert object: {e}")

    def remove(self, obj: T) -> None:
        if obj in self.observable_list:
            self.observable_list.remove(obj)
            self._observableEventRemove([obj])

    def _observableEventAdd(self, added_list: List[T]) -> None:
        print(f"Add event in {self.table_name} table")

    def _observableEventRemove(self, removed_list: List[T]) -> None:
        print(f"Remove event in {self.table_name} table")

        for obj in removed_list:
            try:
                statement = f"DELETE FROM {self.table_name} WHERE {obj.getStringId()} = ?"
                self.model.runStatement(statement, (obj.getId(),))
            except Exception as e:
                raise RuntimeError(f"Failed to delete from database: {e}")

    def _observableEventUpdated(self, target: T) -> None:
        print(f"Update event in {self.table_name} table")

        try:
            self.model.update(
                self.table_name,
                target.getAssociationNameValues(),
                f"{target.getStringId()}={target.getId()}"
            )
        except Exception as e:
            raise RuntimeError(f"Failed to update the database: {e}")

    @abstractmethod
    def getFromResultSet(self, row: sqlite3.Row) -> T:
        pass