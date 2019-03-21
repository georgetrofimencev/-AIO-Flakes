from aiohttp import TCPConnector
from aiohttp.client import ClientSession

from flakes.abstract.source_fetcher import AbstractSourceFetcher


class HabrSourceFetcher(AbstractSourceFetcher):
    def __init__(self, source, tags: list):
        super(AbstractSourceFetcher).__init__(source)
        self.tags = tags

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def fetch_content(self, order_by="date"):
        contents = []
        for tag in self.tags:
            async with ClientSession(
                connector=TCPConnector(verify_ssl=False)
            ) as session:
                content = await self.fetch(
                    session, self.source + f"{tag}&order_by={order_by}"
                )
                contents.append((content, tag))
        return contents

    async def get_contents(self):
        return await self.fetch_content()
