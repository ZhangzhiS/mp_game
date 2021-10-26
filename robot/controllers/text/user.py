#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from werobot.messages.messages import TextMessage

from robot.commons.calculate_exp import get_add_exp
from robot.models.user import User, UserProfile
from robot.msg_reply import message_format, format_userinfo
from robot import state


def creating_role(message: TextMessage, state_session):
    """
    创建角色
    """
    source_openid = message.source
    user = User.objects.get_or_create(openid=source_openid)
    user = user[0]
    user.save()
    if not user.nickname:
        reply = f"""
请设置昵称
昵称中请勿使用非法名称会定期清理违规昵称，维护和谐的游戏环境，谢谢！
(提示:切换公众号菜单按钮到文字输入框回复文字即可)
请回复您的角色昵称(2-8个字符)
"""
        state_session["state"] = state.SET_NICKNAME
        state_session["openid"] = source_openid
        return reply
    try:
        user_profile = UserProfile.objects.get(
            user_id=user.id,
            openid=source_openid,
            user_status=True
        )
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(
            user_id=user.id,
            openid=source_openid,
        )
        user_profile = UserProfile.objects.get(
            user_id=user.id,
            openid=source_openid,
            user_status=True
        )
    study_exp = get_add_exp(state_session)
    user_profile.exp = user_profile.exp + study_exp
    user_profile.save()
    return format_userinfo(user, user_profile, state_session)


def set_nickname(message: TextMessage, state_session):
    """设置昵称"""
    openid = message.source
    nickname = message.content
    if 2 > len(nickname) > 8:
        reply = "提示：角色名长度不符合，请重新回复(2-8个字符):"
        return reply
    user = User.objects.get(openid=openid, status=True)
    user.nickname = message.content
    user.save()
    state_session["state"] = state.SET_GENDER
    reply = f"""
请选择性别
{message_format("男")}|{message_format("女")}
    """
    return reply


def set_gender(message: TextMessage, state_session):
    """设置性别"""
    gender_map = {"男": 1, "女": 2}
    openid = message.source
    gender = message.content
    gender = gender_map.get(gender, 0)
    if not gender:
        reply = f"""请选择性别
{message_format("男")}|{message_format("女")}
        """
        return reply
    user = User.objects.get(openid=openid, status=True)
    if not user:
        return f"请先{message_format('创建角色')}"
    user.gender = gender
    user.save()
    random_gem = random.randint(1000, 2000)
    reply = f"""
色创建成功，欢迎 {message_format(user.nickname)}
我从凡间来，今朝入仙籍。
仙人抚我顶，结发受长生。
看着手中的灵石袋，目送那个缥缈的背影登天而去。
通知：
    仙师给你留下了{random_gem}块灵石！
{message_format("开始修炼")}
"""
    UserProfile.objects.create(
        user_id=user,
        openid=openid,
        gem=random_gem
    )
    user_profile = UserProfile.objects.get(user_id=user.id, openid=openid)
    state_session["exp_add"] = user_profile.exp_add
    state_session["state"] = None
    return reply


def user_info(message: TextMessage, state_session):
    """用户信息"""
    openid = message.source
    try:
        user = User.objects.get()
    except User.DoesNotExist:
        return f"请先  {message_format('创建角色')}"
    user_profile = UserProfile.objects.get(
        user_id=user.id,
        openid=openid,
        user_status=True,
    )
    study_exp = get_add_exp(state_session)
    user_profile.exp = user_profile.exp + study_exp
    user_profile.save()
    reply = format_userinfo(user, user_profile, state_session)
    return reply


def get_all(message):
    print(message.content)
    objs = User.objects.first()
    return objs.openid
