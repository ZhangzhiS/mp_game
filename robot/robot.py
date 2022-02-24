#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
from werobot import WeRoBot
from werobot.config import Config
from werobot.messages.messages import TextMessage
from werobot.session.postgresqlstorage import PostgreSQLStorage

from mp_game.settings import WECHAT_SECRET, WECHAT_APPID, WECHAT_TOKEN
from robot.controllers import session_ctrl
from robot.controllers.text import user
from robot.controllers.text import study


conn = psycopg2.connect(host='42.193.105.229', port='5432', database='mp_game', user='mp_game', password='hsNABfdeL8b3')
session_storage = PostgreSQLStorage(conn)


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


@robot_view.filter("查询用户")
def get_all(message: TextMessage):
    """
    调试查询
    :param message:
    :return:
    """
    resp = user.get_all(message)
    return resp


@robot_view.filter("探索")
def get_all_map(message: TextMessage):
    resp = 1
    return resp
