from src.model.parseDict import ParseDict


class Song(ParseDict):
    def __init__(self):
        self.title = ""
        self.songer = ""
        self.album = ""
        self.long = ""


