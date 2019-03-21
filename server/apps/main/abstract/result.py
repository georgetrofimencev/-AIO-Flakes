from aiohttp import web


class FlakesHTTPResponse(web.Response):
    """Flakes-app Response Object."""
    def __init__(self, result: dict, message: str,
                 status=200, code: int = 0):
        """
        :param result: result-object as a dict
        :param message: response message for client as a string
        :param status: HTTP Status Code(default 200-OK) as a int
        :param code: Backend code for Client as a int
        """
        super().__init__(status=status)
        self.code = code
        self.result = result
        self.message = message

    @property
    def response(self):
        return {
            "code": self.code,
            "data": self.result,
            "message": self.message
        }

    def get_response(self):
        """Returns aiohttp response instance"""
        return web.json_response(data=self.response, status=self.status)


class FlakesErrorException(Exception):
    """Backend Flakes-app Error Exception"""
    status_code = -1  # Not OK

    def __init__(self, status_code, error_message):
        """

        :param status_code:
        :param error_message: Error Message for Client or WebHandler as a string
        """
        super(FlakesErrorException, self).__init__()
        self.status_code = status_code
        self.error_message = error_message
