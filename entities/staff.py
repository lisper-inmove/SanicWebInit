# -*- coding: utf-8 -*-

from mongoengine import StringField

from entities.entity import Entity


class Staff(Entity):

    name = StringField()
