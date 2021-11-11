#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
from werobot.messages.messages import TextMessage

from robot.models import User, LevelConfig, UserProfile, BodyLevelConfig
from robot.msg_reply import format_userinfo

forever_level = "结丹"


def start_study(message: TextMessage, state_session):
    """
    保存当前时间戳
    """
    forever_study = state_session.get("forever_study", False)
    if forever_study:
        return f"已经开始了无尽修炼模式"
    last_status = state_session.get("study_status", False)
    time_step = int(time.time())
    if last_status:
        last_time_step = state_session.get("start_time")
        surplus_time = 300 - (time_step - last_time_step)
        return f"""已经在修炼中了，剩余修炼时间{surplus_time}
达到{forever_level}开启无尽修炼模式"""
    state_session["start_time"] = time_step
    state_session["study_status"] = True
    return "开始修炼！仙路漫漫，修仙路上充满机遇挑战，请努力提升自己！"


def level_up(message: TextMessage, state_session):
    """
    升级
    """
    openid = message.source
    user = User.objects.get(openid=openid, status=True)
    user_profile = UserProfile.objects.get(openid=openid, user_id=user.id)
    user_level = user_profile.level
    user_exp = user_profile.exp
    next_level = LevelConfig.objects.get(last_level=user_level)
    if user_exp < user_profile.next_level_exp:
        return "当前经验不够哦，请继续努力修炼"
    if next_level.body_level_limit > user_profile.body_level:
        return "肉身等级不足，请先提升肉身"
    user_profile.exp = user_profile.exp - user_profile.next_level_exp
    user_profile.level = next_level.level
    user_profile.level_label = next_level.level_label
    user_profile.exp_add += next_level.exp_ampl
    user_profile.next_level_exp = random.randint(next_level.consume_exp_range[0], next_level.consume_exp_range[1])
    user_profile.save()
    state_session["exp_add"] = user_profile.exp_add
    state_session["next_level_limit"] = user_profile.next_level_exp
    return format_userinfo(user, user_profile, state_session)


def body_level_up(message: TextMessage, state_session):
    """"""
    openid = message.source
    user = User.objects.get(openid=openid, status=True)
    user_profile = UserProfile.objects.get(openid=openid, user_id=user.id)
    user_level = user_profile.level
    user_exp = user_profile.exp
    next_level = BodyLevelConfig.objects.get(last_level=user_level)
    if user_exp < user_profile.next_body_level_exp:
        return "当前经验不够哦，请继续努力修炼"
    if next_level.exp_level_limit > user_profile.level:
        return "境界不足，请先提升境界"
    user_profile.exp = user_profile.exp - user_profile.next_body_level_exp
    user_profile.level = next_level.level
    user_profile.level_label = next_level.level_label
    user_profile.exp_add += next_level.exp_ampl
    user_profile.next_body_level_exp = random.randint(next_level.consume_exp_range[0], next_level.consume_exp_range[1])
    user_profile.save()
    state_session["exp_add"] = user_profile.exp_add
    state_session["next_level_limit"] = user_profile.next_level_exp
    return format_userinfo(user, user_profile, state_session)
