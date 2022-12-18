# -*- coding: utf-8 -*-

from base import Base

from mongoengine import StringField


class Book(Base):

    name = StringField()
