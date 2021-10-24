# https://refactoring.guru/design-patterns/chain-of-responsibility/python/example
from __future__ import annotations
from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request):
        pass
