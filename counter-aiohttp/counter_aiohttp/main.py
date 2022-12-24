import asyncio
import logging
from typing import NamedTuple

from aiohttp import web
from aiohttp.web_request import Request
import redis.asyncio as redis
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

REDIS_KEY = 'gio_count'

logger = logging.getLogger(__name__)


async def health(request):
    return web.Response(text="<h1> Async Rest API using aiohttp : Health OK </h1>",
                        content_type='text/html')

async def hook_handler(request: Request):
    async with request.app['redis'].pipeline() as pipeline:
        cur_count, _ = await pipeline.incr(REDIS_KEY).expire(REDIS_KEY, 600).execute()

    # await asyncio.sleep(3)

    logger.info(f'curr count: {cur_count}')
    return web.Response(text=f'OK {cur_count}', content_type='text/plain')

async def hook_sleep_handler(request: Request):
    await asyncio.sleep(3)

    return await hook_handler(request)

async def init_redis(app):
    app['redis'] = connection = redis.Redis()
    await connection.delete(REDIS_KEY)
    yield
    last_count = await connection.get(REDIS_KEY)
    logger.info(f'count: {last_count}')
    await connection.close(close_connection_pool=True)


async def init():
    logging.basicConfig(level=logging.DEBUG)
    #conf = load_config(PROJ_ROOT / 'config' / 'config.yml')

    app = web.Application()
    app.router.add_post('/hook', hook_handler)
    app.router.add_post('/hook/sleep', hook_sleep_handler)
    app.router.add_post('/health', health)
    #redis = await setup_redis(app, conf)

    #host, port = conf['host'], conf['port']
    app.cleanup_ctx.append(init_redis)

    class InitReturn(NamedTuple):
        app: web.Application
        host: str | None
        port: int | None
    return InitReturn(app, None, 8090)


async def create_app():
    """Used by aiohttp-devtools for local development."""
    #import aiohttp_debugtoolbar
    app, _, _ = await init()
    #aiohttp_debugtoolbar.setup(app)
    return app


def main():
    loop = asyncio.get_event_loop()
    # assert isinstance(loop, asyncio.loo)
    app, host, port = loop.run_until_complete(init())
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
