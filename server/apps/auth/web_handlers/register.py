from aiohttp import web
from server.apps.auth.service_handlers.register import RegisterServiceHandler


class RegisterWebHandler(web.View):
    async def post(self):
        """
        requestData: {
            nickname(required as a string),
            password(required as a string),
            telegram_account(no-required as a string),
            tags(massive of tags names as a massive of strings)(no-required),
            sources(massive of resources names as massive of strings)(no-required)
        }
        :return:
            AIOHTTP Response Instance
        """
        async with self.request.app['db'].acquire() as conn:
            data = await self.request.json()
            register_service = RegisterServiceHandler(connection=conn, args=data)
            result = await register_service.post_request_handling()
            response = web.json_response(data=result)
            if result["code"] == 0:
                return response
            else:
                response.set_status(400)
                return response
