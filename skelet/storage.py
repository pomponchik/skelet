from typing import List, Dict, Any
from threading import Lock

from printo import descript_data_object


class Storage:
    __fields__: Dict[str, Any]  # pragma: no cover
    __field_names__: List[str] = []  # pragma: no cover

    def __init__(self, **kwargs: Any) -> None:
        self.__fields__: Dict[str, Any] = {}
        self._lock = Lock()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self) -> str:
        fields_content = {}

        for field_name in self.__field_names__:
            fields_content[field_name] = getattr(self, field_name)

        return descript_data_object(type(self).__name__, (), fields_content)
