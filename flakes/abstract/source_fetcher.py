from abc import ABC, abstractmethod


class AbstractSourceFetcher(ABC):
    def __init__(self, source, tags: list = None):
        self.source = source
        self.tags = tags
        self.content = None

    @abstractmethod
    async def fetch(self, session, url):
        raise NotImplementedError

    @abstractmethod
    async def fetch_content(self, order_by='date'):
        raise NotImplementedError

    @abstractmethod
    def get_contents(self):
        raise NotImplementedError
