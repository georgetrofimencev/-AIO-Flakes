from aiohttp import web
from .web_handlers.register import RegisterWebHandler
from .web_handlers.login import LoginWebHandler


urls = [
        web.post("/register", RegisterWebHandler),
        web.post("/login", LoginWebHandler)
]


def routers(app):
    app.add_routes(urls)

