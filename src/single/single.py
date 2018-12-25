class Singleton:
    __first = True

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst

    def __init__(self):
        if self.__first:
            self.__first = False
            super().__init__()
            self.initUI()

    def initUI(self):
        pass
