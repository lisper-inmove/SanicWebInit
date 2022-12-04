# -*- coding: utf-8 -*-

from sanic.views import HTTPMethodView
from view.unify_response import UnifyResponse

from ctrl import DemoCtrl
from logger.logger import Logger


class Demo(HTTPMethodView):

    name = "Demo"
    uri = "/demo"

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.logger = Logger()
        self.demo_ctrl = DemoCtrl()
        self.demo_ctrl.logger = self.logger

    async def get(self, request):
        result = self.demo_ctrl.get_demo()
        return UnifyResponse.R({"hello": result})
