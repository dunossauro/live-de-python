from file_reader import FileTemplate


class TextFile(FileTemplate):
    def __init__(self, filename):
        self.filename = filename
        self._file = None

    def open_file(self):
        self._file = open(self.filename)

    def close_file(self):
        self._file.close()

    def content(self):
        return self._file.read()
