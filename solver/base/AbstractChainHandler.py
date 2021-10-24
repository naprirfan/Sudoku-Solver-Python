from solver.base.Handler import Handler
from typing import Any, Tuple


class AbstractChainHandler(Handler):
    next_handler: Handler = None

    def set_next(self, handler: Handler):
        self.next_handler = handler
        return handler

    def handle(self, request: Tuple[str, Any]):
        if self.next_handler:
            return self.next_handler.handle(request)

        return None
