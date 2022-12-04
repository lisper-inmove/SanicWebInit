# -*- coding: utf-8 -*-

from ctrl.base_ctrl import BaseCtrl
from dao import DemoDAO


class DemoCtrl(BaseCtrl):

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self._demo_dao = DemoDAO()

    def get_demo(self):
        result = self._demo_dao.get_demo()
        return result
