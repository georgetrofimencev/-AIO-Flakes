from aiohttp import web
from server.apps.auth.service_handlers.login import LoginServiceHandler


class LoginWebHandler(web.View):
    async def post(self):
        """
        {
            nickname(required as a string),
            password(required as a string)
        }
            :return:
            AIOHTTP Response Instance
        """
        async with self.request.app['db'].acquire() as conn:
            data = await self.request.json()
            login_service = LoginServiceHandler(conn, args=data)
            result = await login_service.post_request_handling()
            return result
