#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/11 上午11:12


def get():
    routes = [
        (r'/business_issues', 'base_handler.BaseHandler'),
        (r'/acquire_route', 'base_handler.CalculateHandler'),
        (r'/download_picture', 'base_handler.DownloadRoutePictureHandler')
    ]
    return routes
