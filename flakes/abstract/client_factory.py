from abc import ABC, abstractmethod
from flakes.abstract.content_parser import AbstractContentParser
from flakes.abstract.source_fetcher import AbstractSourceFetcher


class AbstractClientFactory(ABC):

    @abstractmethod
    async def create_source_fetcher(self, user) -> AbstractSourceFetcher:
        raise NotImplementedError

    @abstractmethod
    async def create_content_parser(self, source_fetcher) -> AbstractContentParser:
        raise NotImplementedError
