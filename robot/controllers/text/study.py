#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from werobot.messages.messages import TextMessage


forever_level = "结丹"


def start_study(message: TextMessage, state_session):
    """
    保存当前时间戳
    """
    forever_study = state_session.get("forever_study", False)
    if forever_study:
        return f"已经开始了无尽修炼模式"
    last_status = state_session.get("study_status", True)
    time_step = int(time.time())
    if last_status:
        last_time_step = state_session.get("start_time")
        surplus_time = 300 - (time_step - last_time_step)
        return f"""已经在修炼中了，剩余修炼时间{surplus_time}
达到{forever_level}开启无尽修炼模式"""
    state_session["start_time"] = time_step
    state_session["study_status"] = True
    return "仙路漫漫，修仙路上充满机遇以及危险，请努力提升自己！"


def level_up(message: TextMessage, state_session):
    """"""


def body_level_up(message: TextMessage, state_session):
    """"""
