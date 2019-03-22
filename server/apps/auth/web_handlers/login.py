from aiohttp import web

from server.apps.main.session import session_manager
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
            service = LoginServiceHandler(conn, args=data)
            result = await service.post_request_handling()

            response = web.json_response(data=result)

            if result["code"] == 0:
                return session_manager.set(response, result["user_id"])
            else:
                response.set_status(400)
                return response
