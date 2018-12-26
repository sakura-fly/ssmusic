from src.single.single import Singleton


class MusicApi(Singleton):

    def searchSong(self, keyWord: str, page: int):
        """

        :param keyWord: 查询关键字
        :param page:    页数
        :return:
        """
        pass

    def getLinkById(self, id: str):
        """

        :param id:
        :return:
        """
        pass

    def getSongDetailInfoByIds(self, *id):
        """
        详情
        :param id:
        :return:
        """

    def getAlbumInfoById(self, id: str):
        """
        专辑
        :param id:
        :return:
        """
        pass
