#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werobot.messages.messages import TextMessage
from robot.models.user import User, UserProfile
from robot.msg_reply import message_format, format_userinfo
from robot import state


def creating_role(message: TextMessage, state_session):
    """
    创建角色
    :return:
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
    reply = f"""
色创建成功，欢迎 {message_format(user.nickname)}
新手指引：
1.
2. 
3. 
4.
{message_format("开始修炼")}
"""
    UserProfile.objects.create(
        user_id=user.id,
        openid=openid,
    )
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
    reply = format_userinfo(user, user_profile, state_session)
    return reply


def get_all(message):
    objs = User.objects.first()
    return objs.openid
