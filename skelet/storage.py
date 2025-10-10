from typing import Dict, Any
from threading import Lock

from printo import descript_data_object


class Storage:
    __fields__: Dict[str, Any]  # pragma: no cover

    def __init__(self) -> None:
        self.__fields__: Dict[str, Any] = {}
        self._lock = Lock()
