from abc import ABC, abstractmethod


class AbstractContentParser(ABC):
    def __init__(self, contents=None):
        self.contents = contents

    @abstractmethod
    async def parse_contents(self):
        raise NotImplementedError

    @abstractmethod
    async def parse_content(self, content):
        raise NotImplementedError
