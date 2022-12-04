# -*- coding: utf-8 -*-e

import os
import importlib.util

from sanic import Sanic
from sanic.views import HTTPMethodView

from utils.sysutil import Sysutil


class SanicServer:

    @property
    def app(self):
        return self.__app

    def __init__(self):
        self.__views = list()
        self.__app = self.create_app()
        self.__init_project()
        self.__auto_load_views()

    def __init_project(self):
        self.root_dir = os.path.abspath(os.path.curdir)

    def __auto_load_views(self):
        self.__load_view_from_directory(self.root_dir, "view")

    def __load_view_from_directory(self, root, directory):
        path = os.path.join(root, directory)
        for curroot, dirs, files in os.walk(path):
            for directory in dirs:
                self.__load_view_from_directory(root, directory)
            for file in files:
                filepath = os.path.join(curroot, file)
                self.__load_view_from_file(filepath)

    def __load_view_from_file(self, filename):
        ignore_files = [
            "__init__.py",
            "unify_response.py",
        ]
        for ignore_file in ignore_files:
            if filename.endswith(ignore_file):
                return
        if not filename.endswith("py"):
            return
        spec = importlib.util.spec_from_file_location("test", filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for attribute in module.__dict__.keys():
            if attribute.startswith("__"):
                continue
            view_cls = module.__dict__.get(attribute)
            if view_cls is HTTPMethodView:
                continue
            if not issubclass(view_cls, HTTPMethodView):
                continue
            handler = view_cls()
            self.__views.append(handler)
            self.__app.add_route(handler.as_view(), handler.uri)

    def create_app(self):
        sysutil_helper = Sysutil()
        return Sanic(sysutil_helper.appname)


app = SanicServer().app
