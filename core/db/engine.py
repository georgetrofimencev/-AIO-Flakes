from asyncpgsa import create_pool
import yaml

from config.config import DEFAULT_MODE


async def init_pg(app):
    postgres_conf = app["config"]["postgres"]
    dsn = (
        "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s"
        % postgres_conf
    )
    app["db"] = await create_pool(dsn=dsn)


async def close_pg(app):
    await app["db"].close()


def get_database_uri(mode=None):
    with open(DEFAULT_MODE.parent / f"{mode}.yaml" if mode else DEFAULT_MODE) as conf:
        psql_config = yaml.load(conf)["postgres"]
    return (
        "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s"
        % psql_config
    )
