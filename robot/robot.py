#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from werobot import WeRoBot
from werobot.config import Config
from werobot.messages.messages import TextMessage
from werobot.session.mongodbstorage import MongoDBStorage

from mp_game.settings import WECHAT_SECRET, WECHAT_APPID, WECHAT_TOKEN, MONGODB_URL
from robot import state
from robot.controllers.text import user

collection = pymongo.MongoClient(MONGODB_URL)["wechat"]["session"]
session_storage = MongoDBStorage(collection)


config = Config(
    TOKEN=WECHAT_TOKEN,
    SESSION_STORAGE=session_storage,
    APP_ID=WECHAT_APPID,
    APP_SECRET=WECHAT_SECRET,
)

robot_view = WeRoBot(token=WECHAT_TOKEN, config=config)


@robot_view.text
def set_nickname(message, session):
    """
    设置昵称
    """
    user_state = session.get("state")
    if user_state == state.SET_NICKNAME:
        return user.set_nickname(message, session)
    elif user_state == state.SET_GENDER:
        return user.set_gender(message, session)


@robot_view.filter("创建角色")
def creating_role(message: TextMessage, state_session):
    """
    创建角色
    """
    resp = user.creating_role(message, state_session)
    return resp





@robot_view.filter("开始修炼")
def start_study(message: TextMessage, state_session):
    resp = user.start_study(message, state_session)
    return resp


@robot_view.filter("境界提升")
def level_up(message: TextMessage, state_session):
    resp = user.level_up(message, state_session)
    return resp


@robot_view.filter("肉身提升")
def body_level_up(message: TextMessage, state_session):
    resp = user.body_level_up(message, state_session)
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
