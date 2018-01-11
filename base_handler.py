#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/11 下午12:40

import logging
from tornado.web import RequestHandler
from tsp import tsp_dp


class BaseHandler(RequestHandler):
    def get(self):
        logging.info('show me the data')
        self.render('')


class CalculateHandler(RequestHandler):
    def post(self):
        points = self.get_argument('points')
        d = self.get_argument('d')
        unit = self.get_argument('unit')
        shortest_distance, route = tsp_dp(points, d)
        shortest_distance = str(shortest_distance) + ' ' + unit
        data = dict(shortest_distance=shortest_distance, route=route)
        self.write(data)
