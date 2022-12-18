# -*- coding: utf-8 -*-

from mongoengine import StringField
from mongoengine import BooleanField

from entities.entity import Entity


class StoreConfig(Entity):

    store_id = StringField(unique=True)
    is_head_office = BooleanField()
