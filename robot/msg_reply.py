#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
from urllib.parse import urlencode

from robot.models import MapModel
from robot.models.explore import MapMonster
from robot.models.user import User, UserProfile
import emoji


def message_format(text, show_text=None, msgmenuid=2):
    """格式化为可点击的消息"""
    params = {
        "msgmenucontent": text,
        "msgmenuid": msgmenuid
    }
    url = "weixin://bizmsgmenu?" + urlencode(params)
    return f'<a href="{url}">{show_text or text}</a>'


def format_userinfo(user: User, user_profile: UserProfile, session):
    """格式化返回用户信息"""
    study_status = session.get('study_status', False)
    forever_study = session.get('forever_study', False)
    add_exp = session.get('add_exp')
    study_tag = f"无尽修炼中:每5秒增长的经验为{add_exp}" if forever_study else "修炼中"
    return f"""[ {user.nickname} ] | [ 性别：{'男' if user.gender == 1 else '女'} ]
修为：{user_profile.exp}
修炼速度：{user_profile.exp_add}/每10秒
{study_tag if study_status else message_format("开始修炼", "开始修炼")+"  "+emoji.emojize(":red_heart:")*3}
------------------------
修为：
    当前境界:{user_profile.level_label}
    升级需求:{user_profile.next_level_exp}
    {message_format("境界提升", "境界提升")}
------------------------
肉身：
    当前境界:{user_profile.body_level_label}
    升级需求:{user_profile.next_body_level_exp}
    {message_format("肉身提升", "境界提升")}
------------------------
功能：
{message_format('角色')}|{message_format('物品')}|{message_format("探险")}|{"修炼中" if study_status else message_format("开始修炼", "修炼")+"  "+emoji.emojize(":red_heart:")*3}
------------------------
"""


"""
# ------------------------
# 属性：
# 生命值:{user_profile.health_point}/{user_profile.max_health_point}
# 法力值:{user_profile.mana_point}/{user_profile.max_mana_point}
# 力量:{user_profile.strength}    敏捷:{user_profile.dexterity}
# 智力:{user_profile.intelligence}    体力:{user_profile.intelligence}
# 护甲:{user_profile.armor}
# {message_format("详细属性")}
------------------------
装备：
------------------------
功能：
{message_format('角色')}|{message_format("技能")}|{message_format('物品')}|{message_format("探险")}|{"修炼中" if study_status else message_format("开始修炼", "修炼")+"  "+emoji.emojize(":red_heart:")*3}
------------------------
"""


def format_maps(maps: List[MapModel], operation="选择地图"):

    def gen_msg(t_m: List[str]):
        m = ""
        for it in t_m:
            m = m + message_format(text=f"{operation}-{it}", show_text=it) + "    "
        m += "\n"
        return m

    res = "可探索地图列表：\n"
    tmp_map = []
    for map_obj in maps:
        if len(tmp_map) == 3:
            res += gen_msg(tmp_map)
            tmp_map = []
        tmp_map.append(map_obj.name)
    res += gen_msg(tmp_map)
    return res


def format_map_detail(map: MapModel, monsters: List[MapMonster]):
    res =  f"""地图：{map.name}
{map.desc if map.desc else None}
耗时：{map.consume_time}秒
"""
    if monsters:
        res += "怪物：\n"
    for monster in monsters:
        res += f"{monster.monster_id.name}\n"
    return res


if __name__ == '__main__':

    a = message_format("hello")
    print(a)
