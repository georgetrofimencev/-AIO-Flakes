from server.apps.main.abstract.result import FlakesHTTPResponse
from server.apps.main.abstract.service import AbstractPostServiceHandler
from server.apps.main.abstract.result import FlakesErrorException
from core.managers.user_manager import UserManager


class RegisterServiceHandler(AbstractPostServiceHandler):
    def __init__(self, connection, args: dict):
        _required_fields = {
            "nickname": str,
            "password": str,
        }
        super().__init__(connection, args, _required_fields)

    async def post_request_handling(self):
        #  TODO: Завернуть в декоратор
        #  Загромождает метод, тем более в каждом сервсином обработчике
        #  Будет одно и то же действие(don't repeat yourself(DRY))
        if await self._is_valid_request:
            try:
                result = await self._prepare_result()
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

    async def _prepare_result(self):
        user_manager = UserManager(self.connection)
        return await user_manager.register_user(**self.args)
