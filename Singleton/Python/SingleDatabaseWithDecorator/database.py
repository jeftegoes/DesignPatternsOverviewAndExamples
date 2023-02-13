from singleton import singleton


@singleton
class Database:
    def __init__(self):
        print('Loading database')
