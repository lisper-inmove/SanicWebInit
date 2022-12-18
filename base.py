# -*- coding: utf-8 -*-


class Base:

    def __getattr__(self, key):
        return self.__dict__.get(key)

    def __setattr__(self, key, value):
        self.__dict__.update({key: value})
