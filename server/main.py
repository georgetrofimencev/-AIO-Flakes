import sys
from aiohttp import web
from server.apps.main.app import create_app


def main(mode):
    app = create_app(mode)
    web.run_app(app)


if __name__ == '__main__':
    main(sys.argv[1:])
