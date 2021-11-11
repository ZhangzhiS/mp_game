#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import urlencode

import emoji


def message_format(text, show_text=None, msgmenuid=2):
    """格式化为可点击的消息"""
    params = {
        "msgmenucontent": text,
        "msgmenuid": msgmenuid
    }
    url = "weixin://bizmsgmenu?" + urlencode(params)
    return f'<a href="{url}">{show_text or text}</a>'


def format_userinfo(user, user_profile, session):
    """格式化返回用户信息"""
    study_status = session.get('study_status', False)
    forever_study = session.get('forever_study', False)
    add_exp = session.get('add_exp')
    study_tag = f"无尽修炼中:每5秒增长的经验为{add_exp}" if forever_study else "修炼中"
    return f"""[ {user.nickname} ] | [ 性别：{'男' if user.gender == 1 else '女'} ]
修为：{user_profile.exp}
修炼速度：{user_profile.exp_add}/每10秒
{study_tag if study_status else message_format("开始修炼", "修炼")+"  "+emoji.emojize(":red_heart:")*3}
------------------------
修为：
    当前境界:{user_profile.level_label}
    升级需求:{user_profile.next_level_exp}
    {message_format("境界提升", "升级")}
------------------------
肉身：
    当前境界:{user_profile.body_level_label}
    升级需求:{user_profile.next_body_level_exp}
    {message_format("肉身提升", "升级")}
------------------------
功能：
{message_format('角色')}|{message_format("技能")}|{message_format('物品')}|{message_format("探险")}|{"修炼中" if study_status else message_format("开始修炼", "修炼")+"  "+emoji.emojize(":red_heart:")*3}
------------------------
"""


if __name__ == '__main__':

    a = message_format("hello")
    print(a)
