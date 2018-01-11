#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/11 下午12:40

import logging
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def get(self):
        logging.info('show me the data')
        self.write('')


class DownloadHandler(RequestHandler):
    def post(self):
        pass

