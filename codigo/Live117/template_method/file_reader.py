from abc import ABC, abstractmethod


class FileTemplate(ABC):
    def read_file(self):
        self.open_file()
        content = self.content()
        self.close_file()
        return content

    @abstractmethod
    def open_file(self):
        ...

    @abstractmethod
    def close_file(self):
        ...

    @abstractmethod
    def content(self):
        ...
