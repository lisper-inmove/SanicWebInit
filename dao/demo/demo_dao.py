# -*- coding: utf-8 -*-

from dao.base_dao import BaseDAO


class DemoDAO(BaseDAO):

    def get_demo(self):
        return "Get Demo"
