from datetime import date, datetime
from typing import Optional

class DateUtils:
    @staticmethod
    def getToString(date_obj: Optional[date]) -> str:
        if date_obj is None:
            return ""
        return date_obj.strftime("%d/%m/%Y")

    @staticmethod
    def fromString(date_str: str) -> Optional[date]:
        try:
            return datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            return None

    @staticmethod
    def getCurrentDate() -> date:
        return date.today()