#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import random
import time
from typing import List

from werobot.messages.messages import TextMessage
import redis

from robot import models
from robot.commons.user_common import get_user_obj
from robot.msg_reply import format_map_detail, format_maps

db = redis.Redis()


def gen_monster(monster_objs: List[models.MapMonster]):
    res = []
    for monster_config in monster_objs:
        count = random.randint(monster_config.count[0], monster_config.count[1])
        res.extend([monster_config.monster_id] * count)
    return res


def auto_fighting(openid, map_id):
    map = models.MapModel.objects.get(id=map_id)
    _, user_info = get_user_obj(openid)


def get_maps(message: TextMessage, state_session):
    maps = models.MapModel.objects.all()
    res = format_maps(maps)
    explore_status = state_session.get("explore_status", 0)
    if not explore_status:
        return res
    end_time = state_session.get("explore_end_time")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if end_time > now:
        res += f"""------------------------\n提示：\n正在探索中，预计{end_time}结束 """
        return res
    return res


def time_f(need_time):
    now = datetime.datetime.now()
    end_time = now + datetime.timedelta(seconds=need_time)
    return end_time.strftime("%Y-%m-%d %H:%M:%S")


def build_map_detail(map):
    map_monsters = map.mapmonster_set.filter(status=True)
    monsters_name = [i.monster_id.name for i in map_monsters]
    award = ["灵石"]
    for monster in map_monsters:
        eqs = monster.monster_id.award_eq.all()
        eq_names = [i.name for i in eqs]
        award.extend(eq_names)
    res = format_map_detail(map, monsters_name, award)
    return res


def get_map_detail(message, state_session):
    select_map = message.content
    map_name = select_map.split("-")[1]
    try:
        map_obj = models.MapModel.objects.get(name=map_name)
    except models.MapModel.DoesNotExist:
        maps = models.MapModel.objects.all()
        return f"""请选择正确的探索地图
{format_maps(maps)}
"""
    map_detail = db.get(map_name)
    if not map_detail:
        map_detail = build_map_detail(map_obj)
        db.set(map_name, map_detail)
    return map_detail


def do_explore(message: TextMessage, state_session):
    """选择地图进行探索"""
    explore_map = message.content
    map_name = explore_map.split("-")[1]
    try:
        map_obj = models.MapModel.objects.get(name=map_name)
    except models.MapModel.DoesNotExist:
        maps = models.MapModel.objects.all()
        return f"""请选择正确的探索地图
{format_maps(maps, "探索地图")}
"""
    # TODO 校验拥有的灵石是否足够去探索，并减少相应的灵石
    if map_obj.consume_gem:
        openid = message.source
        _, user_info = get_user_obj(openid)
        if user_info.gem < map_obj.consume_gem:
            return "灵石数量不够，无法进行探索当前选择的地图"
        user_info.gem -= map_obj.consume_gem
        user_info.save()
    end_time = time_f(map_obj.consume_time)
    state_session["explore_start"] = int(time.time())
    state_session["explore_map"] = map_obj.id
    state_session["explore_consume_time"] = map_obj.consume_time
    state_session["explore_end_time"] = end_time
    state_session["explore_status"] = 1
    return f"""已开始探索 {map_obj.name} 预计：
    {end_time} 结束"""
