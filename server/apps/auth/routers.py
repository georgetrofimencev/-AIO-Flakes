from aiohttp import web
from .web_handlers.register import RegisterWebHandler


def routers(app):
    app.add_routes([web.post("/register", RegisterWebHandler)])
