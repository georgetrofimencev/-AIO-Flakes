import base64
import uvloop
import asyncio
import aiohttp_debugtoolbar

from cryptography import fernet

from aiohttp import web
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from core.db.engine import init_pg, close_pg
from config.config import load_config

from .routers import setup_routers


async def create_app(mode):
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app = web.Application()
    app['config'] = load_config(mode)

    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    aiohttp_debugtoolbar.setup(app)
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))
    setup_routers(app)

    return app
