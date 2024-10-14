from singleton import Singleton


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')
