"""
this module is created to demonstrate the Singleton Design Pattern;
"""
import sqlite3


def singleton(cls):
    """
    this functions will serve as decorator;
    takes a class object as arg;
    """
    _instances = [None]

    def wrapper(*args, **kwargs):
        if _instances[0] is None:
            _instances[0] = cls(*args, **kwargs)
        return _instances[0]
    return wrapper


@singleton
class ApplicationDb(object):
    """
    used for opening/querying/closing an Sqlite database;
    it is decorated with the singleton decorator;
    """
    def __init__(self):
        self.__connx = None
        self.curr = None

    def open_conn(self, db_path: str):
        try:
            self.__connx = sqlite3.connect(db_path)
        except IOError:
            print('Db not found.')

    def open_cursor(self):
        try:
            self.curr = self.__connx.cursor()
        except IOError:
            pass

    def query_db(self, qry_string: str):
        query_res = self.curr.execute(qry_string).fetchall()
        return query_res

    def __del__(self):
        self.__connx.close()



