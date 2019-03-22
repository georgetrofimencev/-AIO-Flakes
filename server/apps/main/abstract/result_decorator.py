from server.apps.main.abstract.exceptions import FlakesErrorException


def post_handling(handler_method):
    async def wrapper(self, *args, **kwargs):
        if await self._is_valid_request:
            try:
                self.result = await handler_method(self, *args, **kwargs)
                self.result["code"] = 0
            except FlakesErrorException as e:
                self.result = {
                    "requestData": self.args,
                    "message": e.error_message,
                    "code": e.status_code,
                }
        else:
            self.result = {
                "requestData": self.args,
                "message": "Invalid Request Data.",
                "code": -1,
            }
        return self.result
    return wrapper
