#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import redis
from werobot import WeRoBot
from werobot.config import Config
from werobot.messages.messages import TextMessage
from werobot.session.redisstorage import RedisStorage

from mp_game.settings import WECHAT_SECRET, WECHAT_APPID, WECHAT_TOKEN
from robot.controllers import session_ctrl
from robot.controllers.text import user
from robot.controllers.text import study
from robot.controllers.text import explore
from robot.commons.chat import gen_res

db = redis.Redis()
session_storage = RedisStorage(db, prefix="mp_game")


config = Config(
    TOKEN=WECHAT_TOKEN,
    SESSION_STORAGE=session_storage,
    APP_ID=WECHAT_APPID,
    APP_SECRET=WECHAT_SECRET,
)

robot_view = WeRoBot(token=WECHAT_TOKEN, config=config)


@robot_view.text
def state_handler(message, session):
    """
    关于state不同状态的处理
    """
    print(message.content)
    res = gen_res(message.content)
    return res
    res = session_ctrl.session_options(message, session)
    if res:
        return res


@robot_view.filter("创建角色")
def creating_role(message: TextMessage, state_session):
    resp = user.creating_role(message, state_session)
    return resp


@robot_view.filter("角色信息")
def get_user_info(message: TextMessage, state_session):
    resp = user.user_info(message, state_session)
    return resp


@robot_view.filter("开始修炼")
def start_study(message: TextMessage, state_session):
    resp = study.start_study(message, state_session)
    return resp


@robot_view.filter("境界提升")
def level_up(message: TextMessage, state_session):
    resp = study.level_up(message, state_session)
    return resp


@robot_view.filter("肉身提升")
def body_level_up(message: TextMessage, state_session):
    resp = study.body_level_up(message, state_session)
    return resp


@robot_view.filter("探索")
def explore_route(message: TextMessage, state_session):
    resp = explore.get_maps(message, state_session)
    return resp


@robot_view.filter(re.compile(r"选择地图-.*?"))
def explore_select_map(message: TextMessage, state_session):
    resp = explore.get_map_detail(message, state_session)
    return resp


@robot_view.filter(re.compile(r"探索地图-.*?"))
def explore_map(message: TextMessage, state_session):
    resp = explore.do_explore(message, state_session)
    return resp


@robot_view.filter("查询用户")
def get_all(message: TextMessage):
    """
    调试查询
    :param message:
    :return:
    """
    resp = user.get_all(message)
    return resp
