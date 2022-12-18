# -*- coding: utf-8 -*-

from mongoengine import StringField
from mongoengine import ListField

from entities.entity import Entity


class Category:

    name = StringField()
    # 书籍ID列表，其中的索引表示了书籍在分类中的顺序
    books = ListField()
