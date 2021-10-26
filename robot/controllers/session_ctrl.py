#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werobot.messages.messages import TextMessage

from robot import state
from robot.commons.user_common import get_user_obj
from robot.controllers.text import user
from robot.msg_reply import message_format


def _check_session_openid(message: TextMessage, session):
    openid = session.get("openid")
    if not openid:
        openid = message.source
        user_obj, user_profile_obj = get_user_obj(openid)
        if not user_obj:
            if message.content == "创建角色":
                return user.creating_role(message, session)
            return f"请先{message_format('创建角色')}"
        session["openid"] = openid
    return ""


def _check_session_state(message: TextMessage, session):
    user_state = session.get("state")
    if user_state == state.SET_NICKNAME:
        return user.set_nickname(message, session)
    elif user_state == state.SET_GENDER:
        return user.set_gender(message, session)
    return ""


def session_options(message: TextMessage, session):
    """
    关于session的处理
    1. 首先判断session中，是否存在openid，如果不存在，则可能是用户没有注册，则提示用户注册
    """
    openid_status_res = _check_session_openid(message, session)
    if openid_status_res:
        return openid_status_res
    state_res = _check_session_state(message, session)
    if state_res:
        return state_res
