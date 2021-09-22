#!/usr/bin/env python
# -*- coding: utf-8 -*-
from robot.robot import robot_view


@robot_view.subscribe()
def subscribe(message):
    """
    关注
    :param message:
    :return:
    """
    return "欢迎关注"
