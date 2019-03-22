from abc import ABC, abstractmethod


class AbstractServiceHandler(ABC):
    """Abstract handler for handling request data.
       Checking request validity, preparing work's response.
    """
    def __init__(self, connection):
        """
        :param connection:
        """
        self.connection = connection

    @abstractmethod
    async def _is_valid_request(self):
        raise NotImplementedError

    @abstractmethod
    async def _prepare_response(self):
        raise NotImplementedError


class AbstractGetServiceHandler(AbstractServiceHandler):
    """Abstract Service handler for handling GET Requests"""
    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    async def get_result_handling(self):
        raise NotImplementedError


class AbstractPostServiceHandler(AbstractServiceHandler):
    """Abstract Service handler for handling POST Requests"""
    def __init__(self, connection, args, required_fields):
        super().__init__(connection)
        self.args = args
        self._required_fields = required_fields

    @abstractmethod
    async def post_request_handling(self):
        raise NotImplementedError

    @property
    async def _is_valid_request(self):
        for _field in self._required_fields:
            if _field not in self.args:
                return False
        return True

