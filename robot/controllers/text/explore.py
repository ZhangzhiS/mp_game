#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import random
import time
from typing import List

from werobot.messages.messages import TextMessage

from robot import models
from robot.msg_reply import format_maps


def gen_monster(monster_objs: List[models.MapMonster]):
    """"""
    res = []
    for monster_config in monster_objs:
        count = random.randint(monster_config.count[0], monster_config.count[1])
        res.extend([monster_config.monster_id] * count)
    return res


def auto_fighting(user_profile: models.UserProfile, all_monsters: List[models.MonsterConfig]):
    pass


def get_maps(state_session):
    """"""
    maps = models.MapModel.objects.all()
    res = format_maps(maps)
    explore_status = state_session.get("explore_status", 0)
    if not explore_status:
        return res
    end_time = state_session.get("explore_end_time")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if end_time < now:
        res += f"""------------------------\n提示：\n正在探索中，预计{end_time}结束 """
        return res
    return res


def time_f(need_time):
    now = datetime.datetime.now()
    end_time = now + datetime.timedelta(seconds=need_time)
    return end_time.strftime("%Y-%m-%d %H:%M:%S")


def do_explore(message: TextMessage, state_session):
    """选择地图进行探索"""
    explore_map = message.content
    map_name = explore_map.split("-")[1]
    try:
        map_obj = models.MapModel.objects.get(name=map_name)
    except models.MapModel.DoesNotExist:
        maps = models.MapModel.objects.all()
        return f"""
请选择正确的探索地图
{format_maps(maps)}
"""
    end_time = time_f(map_obj.consume_time)
    state_session["explore_start"] = int(time.time())
    state_session["explore_map"] = map_obj.id
    state_session["explore_consume_time"] = map_obj.consume_time
    state_session["explore_end_time"] = end_time
    state_session["explore_status"] = 1
    return f"""已开始探索 {map_obj.name} 预计：
    {end_time} 结束"""
