from flakes.abstract.client_factory import AbstractClientFactory
from flakes.clients.habr.fetcher import HabrSourceFetcher
from flakes.clients.habr.parser import HabrContentParser


class HabrClientFactory(AbstractClientFactory):
    source = 'https://habr.com/ru/search/?target_type=posts&q='

    def __init__(self, user):
        self.user = user

    async def create_source_fetcher(self, user):
        return HabrSourceFetcher(source=self.source, tags=user.tags)

    async def create_content_parser(self, source_fetcher: HabrSourceFetcher):
        contents = await source_fetcher.get_contents()
        return HabrContentParser(contents)
