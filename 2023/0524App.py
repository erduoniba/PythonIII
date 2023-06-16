import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

# 异步框架aiohttp：
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1 style="color:red;">Awesome</h1>', content_type='text/html')

async def init(loop):
    app = web.Application()
    app.add_routes([web.get("/", index)])
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9090)
    logging.info('server started at http://127.0.0.1:9090')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()