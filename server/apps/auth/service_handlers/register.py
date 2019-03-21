from server.apps.main.abstract.result import FlakesHTTPResponse
from server.apps.main.abstract.service import AbstractPostServiceHandler
from server.apps.main.abstract.result import FlakesErrorException
from core.managers.user_manager import UserManager


class RegisterServiceHandler(AbstractPostServiceHandler):
    def __init__(self, connection, args: dict):
        super().__init__(connection, args)
        self._required_fields = {
            "nickname": str,
            "password": str,
        }

    async def post_result_handling(self):
        #  TODO: Завернуть в декоратор
        if await self._is_valid_request:
            try:
                result = await self._prepare_response()
                http_response = FlakesHTTPResponse(
                    result=result,
                    message='Success user register'
                )
            except FlakesErrorException as e:
                http_response = FlakesHTTPResponse(
                    result={},
                    message=f'{e.error_message}',
                    code=e.status_code
                )
        else:
            http_response = FlakesHTTPResponse(
                result={},
                message='Bad request data',
                status=400,
                code=-1
            )
        return http_response.get_response()

    @property
    async def _is_valid_request(self):
        for _field in self._required_fields:
            if _field not in self.args:
                return False
        return True

    async def _prepare_response(self):
        user_manager = UserManager(self.connection)
        return await user_manager.register_user(**self.args)
