import importlib


def setup_routers(main_app):
    [
        importlib.import_module(f"server.apps.{app}.routers").routers(main_app)
        for app in main_app["config"]["apps"]
    ]
