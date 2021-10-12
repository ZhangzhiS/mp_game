#!/usr/bin/env python
# -*- coding: utf-8 -*-
from robot.models.user import User, UserProfile
import emoji


def message_format(text, show_text=None):
    """格式化为可点击的消息"""
    return f'<a href="weixin://bizmsgmenu?msgmenucontent={text}&msgmenuid=2">{show_text or text}</a>'


def format_userinfo(user: User, user_profile: UserProfile, session):
    """格式化返回用户信息"""
    study_status = session.get('study_status', False)
    forever_study = session.get('forever_study', False)
    add_exp = session.get('add_exp')
    study_tag = f"无尽修炼中:每5秒增长的经验为{add_exp}" if forever_study else "修炼中"
    return f"""[ {user.nickname} ] | [ 性别：{'男' if user.gender == 1 else '女'} ]
修为：{user_profile.exp}
修炼速度：{user_profile.exp_add}/每10秒
{study_tag if study_status else message_format("开始修炼", "修炼")+"  "+emoji.emojize(":red_heart:")*3}
     当前境界       | 升级需求
境界：{user_profile.level_label} | {100000} | {message_format("境界提升", "升级")}
肉身：{user_profile.body_level_label} | {100000} | {message_format("肉身提升", "升级")}
------------------------
属性：
生命值:{user_profile.health_point}/{user_profile.max_health_point}
法力值:{user_profile.mana_point}/{user_profile.max_mana_point}
力量:{user_profile.strength}    敏捷:{user_profile.dexterity}
智力:{user_profile.intelligence}    体力:{user_profile.intelligence}
护甲:{user_profile.armor}
{message_format("详细属性")}
------------------------
装备：
------------------------
功能：
{message_format('角色')}|{message_format("技能")}|{message_format('物品')}|{message_format("探险")}|{"修炼中" if study_status else message_format("开始修炼", "修炼")+"  "+emoji.emojize(":red_heart:")*3}
------------------------
"""
