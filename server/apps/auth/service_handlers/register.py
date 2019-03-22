from server.apps.main.abstract.service import AbstractPostServiceHandler
from server.apps.main.abstract.result_decorator import post_handling
from core.managers.user_manager import UserManager


class RegisterServiceHandler(AbstractPostServiceHandler):
    def __init__(self, connection, args: dict):
        _required_fields = {
            "nickname": str,
            "password": str,
        }
        super().__init__(connection, args, _required_fields)

    @post_handling
    async def post_request_handling(self):
        return await self._prepare_result()

    async def _prepare_result(self):
        user_manager = UserManager(self.connection)
        return await user_manager.register_user(**self.args)
