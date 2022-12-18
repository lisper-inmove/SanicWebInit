# -*- coding: utf-8 -*-

from mongoengine import StringField
from mongoengine import ListField

from entities.entity import Entity


class Store(Entity):

    name = StringField()
    branches = ListField()
