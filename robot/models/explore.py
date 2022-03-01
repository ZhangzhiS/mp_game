#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
探索
"""
from django.db import models
from django.contrib.postgres.fields import IntegerRangeField

from robot.models.base_class import BaseModel
from robot.models.equipment import EqModel


class MonsterConfig(BaseModel):
    name = models.CharField(max_length=255, verbose_name="名字")
    health_point = IntegerRangeField(verbose_name="血量范围")
    attack = IntegerRangeField(verbose_name="攻击力范围")
    defense = IntegerRangeField(verbose_name="防御力范围")
    award_gem = IntegerRangeField(verbose_name="灵石奖励")
    award_eq = models.ManyToManyField(
        verbose_name="可能掉落的装备",
        to=EqModel
    )

    class Meta:
        verbose_name = "怪物"
        verbose_name_plural = verbose_name


class MapModel(BaseModel):
    map_type = [
        ("凡间", "1")
    ]
    name = models.CharField(max_length=255, verbose_name="名字")
    desc = models.CharField(max_length=255, verbose_name="描述", default="")
    consume_gem = models.IntegerField(verbose_name="消耗灵石")
    consume_time = models.IntegerField(verbose_name="探索消耗的时间，单位（秒）", default=1)

    class Meta:
        verbose_name = "地图"
        verbose_name_plural = verbose_name


class MapMonster(BaseModel):
    map_id = models.ForeignKey(
        to=MapModel,
        on_delete=models.SET_NULL,
        verbose_name="地图",
        null=True
    )
    monster_id = models.ForeignKey(
        to=MonsterConfig,
        on_delete=models.SET_NULL,
        verbose_name="怪物",
        null=True
    )
    count = IntegerRangeField(verbose_name="存在怪物的数量")
    status = models.BooleanField(default=True, verbose_name="是否有效配置")

    class Meta:
        verbose_name = "地图怪物配置"
        verbose_name_plural = verbose_name

    def to_dict(self, exclude=None):
        return {
            "monster_id": self.monster_id.id,
            "monster_name": self.monster_id.name,
            "count": self.count,
        }
