class Singleton:
    __have = False

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst

    def __init__(self):
        if not self.__have:
            self.__have = True
            super().__init__()
            self.initUI()

    def initUI(self):
        pass
