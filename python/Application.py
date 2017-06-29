#!/bin/env /usr/bin/python2

class Application:

    def __init__(self, name, executable, icon="", cliArgs='', runInTerm=False, *args, **kwargs):
        self.__name__(self, name)
        self.__exec__(self, executable)
        self.__icon__(self, icon)
        self.__clop__(self, cliArgs)
        self.__rit__(self, runInTerm)

    @property
    def __name__(self):
        return self.__name__
    @__name__.setter
    def __name__(self, value):
        self.__name__ = value

    @property
    def __exec__(self):
        return self.__exec__
    @__exec__.setter
    def __exec__(self, value):
        self.__exec__ = value

    @property
    def __clop__(self):
        return self.__clop__
    @__clop__.setter
    def __clop__(self, value):
        self.__clop__ = value

    @property
    def __icon__(self):
        return self.__icon__
    @__icon__.setter
    def __icon__(self, value):
        self.__icon__ = value

    @property
    def __rit__(self):
        return self.__rit__
    @__rit__.setter
    def __rit__(self, value):
        self.__rit__ = value

    @property
    def __media__(self):
        return self.__media__
    @__media__.setter
    def __media__(self, value):
        self.__media__ = value
