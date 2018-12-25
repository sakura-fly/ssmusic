class ParseDict:

    # 从字典赋值
    def fromDict(self, songMsg: dict):
        __dict = self.__dict__
        for k in __dict.keys():
            self.__setattr__(k, songMsg.get(k) if songMsg.get(k) else "")
        return self
