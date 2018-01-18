#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/11 上午11:12


def get():
    routes = [
        (r'/', 'base_handler.BaseHandler'),
        (r'/acquire_route', 'base_handler.CalculateHandler'),
        (r'/draw_points', 'base_handler.DrawPointsHandler'),
        (r'/download_picture', 'base_handler.DownloadRoutePictureHandler')
    ]
    return routes
