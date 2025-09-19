from abc import ABC, abstractmethod
from typing import List, Dict, Any

class GeneralType(ABC):
    @abstractmethod
    def copyWithDiffId(self, id: int) -> 'GeneralType':
        pass

    @abstractmethod
    def getId(self) -> int:
        pass

    @abstractmethod
    def getStringId(self) -> str:
        pass

    @abstractmethod
    def getProperties(self) -> List[Any]:
        pass

    @abstractmethod
    def getPropertiesType(self) -> Dict[Any, str]:
        pass
    def getTupleName(self) -> str:
        return ""

    def getTupleValues(self) -> str:
        return ""

    def getAssociationNameValues(self) -> str:
        return ""
