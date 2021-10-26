#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from typing import List

from werobot.messages.messages import TextMessage

from robot import models
from robot.msg_reply import format_maps


def get_maps(message: TextMessage):
    """"""
    maps = models.MapModel.objects.all()
    res = format_maps(maps)
    return res


def gen_monster(monster_objs: List[models.MapMonster]):
    """"""
    res = []
    for monster_config in monster_objs:
        count = random.randint(monster_config.count[0], monster_config.count[1])
        res.extend([monster_config.monster_id] * count)
    return res


def auto_fighting(user_profile: models.UserProfile, all_monsters: List[models.MonsterConfig]):

    pass


def do_explore(message: TextMessage, state_session):
    """"""
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
    map_monsters = map_obj.mapmonster_set.filter(status=True)
    all_monsters = gen_monster(map_monsters)
