from typing import Any
from abc import ABC, abstractmethod
from typing import TypeVar, Type, Any

from simtypes import check


class SecondNone:
    pass

ExpectedType = TypeVar('ExpectedType')

class AbstractSource(ABC):
    @abstractmethod
    def __getitem__(self, key: str) -> Any:
        ...  # pragma: no cover

    def get(self, key: str, default: Any = SecondNone()) -> ExpectedType:
        try:
            result = self[key]
        except KeyError:
            if not isinstance(default, SecondNone):
                return default
            raise

        return result

    def type_awared_get(self, key: str, hint: Type[ExpectedType], default: Any = SecondNone()) -> ExpectedType:
        result = self.get(key, default)

        if result is default:
            if not isinstance(default, SecondNone):
                return default
            raise KeyError(key)

        if not check(result, hint, strict=True):
            raise TypeError(f'The value of the "{key}" field did not pass the type check.')

        return result
