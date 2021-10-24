from solver.base.Handler import Handler
from abc import abstractmethod
from typing import Any


class AbstractChainHandler(Handler):
    next_handler: Handler = None

    @abstractmethod
    def set_next(self, handler: Handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any):
        if self.next_handler:
            return self.next_handler.handle(request)

        return None
