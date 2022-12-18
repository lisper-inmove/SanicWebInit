# -*- coding: utf-8 -*-

from mongoengine import Document
from mongoengine import StringField


class Entity(Document):

    id = StringField(unique=True)
