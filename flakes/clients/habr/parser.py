from bs4 import BeautifulSoup
from flakes.abstract.content_parser import AbstractContentParser


class HabrContentParser(AbstractContentParser):

    def __init__(self, contents):
        super(AbstractContentParser).__init__(contents)

    async def parse_contents(self):
        for content in self.contents:
            await self.parse_content(content)

    async def parse_content(self, content: tuple):
        """
        :param content: tuple(tag, html)
        :return:
        """
        soap = BeautifulSoup(content[0], 'lxml')
