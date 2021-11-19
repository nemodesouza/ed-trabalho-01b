class Element:

    def __init__ (self, data):
        self.__data = data
        self.__prev = None

    @property
    def data(self):
        return self.__data

    @property
    def prev(self):
        return self.__prev

    @data.setter
    def data(self, data):
        self.__data = data

    @prev.setter
    def prev(self, prev):
        self.__prev = prev
