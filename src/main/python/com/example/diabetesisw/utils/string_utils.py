from typing import Optional

class StringUtils:
    @staticmethod
    def capitalize(text: Optional[str]) -> str:
        if text is None or len(text) == 0:
            return ""
        return text[0].upper() + text[1:].lower() if len(text) > 1 else text.upper()