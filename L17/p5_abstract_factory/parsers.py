from abc import ABC, abstractmethod

from bs4 import BeautifulSoup


class Parser(ABC):

    @abstractmethod
    def __call__(self, content):
        pass


class HTTPParser(Parser):
    def __call__(self, content):
        filenames = []
        soup = BeautifulSoup(content, "html.parser")
        links = soup.find_all('a')
        for link in links:
            filenames.append(link.text)
        return '\n'.join(filenames)


class FTPParser(Parser):
    def __call__(self, content):
        content = content.decode('utf-8')
        lines = content.split('\n')
        filenames = []
        for line in lines:
            split_line = line.split(None, 8)
            if len(split_line) == 9:
                filenames.append(split_line[-1])
        return '\n'.join(filenames)
