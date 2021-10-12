#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

from robot.models.base_class import BaseModel


class User(BaseModel):
    """用户"""
    openid = models.CharField(max_length=255, verbose_name="用户的openid", db_index=True)
    nickname = models.CharField(max_length=32, verbose_name="用户的昵称")
    sub_time = models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name="注册时间")
    gender = models.IntegerField(null=True, verbose_name="性别, 1:男，2:女")
    status = models.BooleanField(default=True, verbose_name="用户状态")


class UserProfile(BaseModel):
    """用户属性"""
    user_id = models.ForeignKey(
        verbose_name="用户的id",
        to=User,
        to_field="id",
        on_delete=models.SET_NULL,
        null=True
    )
    openid = models.CharField(max_length=255, verbose_name="用户的openid", db_index=True)
    level = models.IntegerField(verbose_name="境界", default=1)
    level_label = models.CharField(max_length=100, verbose_name="境界展示名称", default="筑基一阶")
    body_level = models.IntegerField(verbose_name="肉身", default=1)
    body_level_label = models.CharField(max_length=100, verbose_name="身体等级展示名称", default="铁骨一阶")
    exp = models.BigIntegerField(verbose_name="当前修为", default=0)
    exp_add = models.IntegerField(verbose_name="每秒修为增长数量", default=5)
    max_health_point = models.IntegerField(verbose_name="最大生命值", default=100)
    health_point = models.IntegerField(verbose_name="当前生命值", default=100)
    max_mana_point = models.IntegerField(verbose_name="最大法力值", default=100)
    mana_point = models.IntegerField(verbose_name="当前法力值", default=100)
    strength = models.IntegerField(verbose_name="力量", default=5)
    dexterity = models.IntegerField(verbose_name="敏捷", default=5)
    intelligence = models.IntegerField(verbose_name="智力", default=5)
    vitality = models.IntegerField(verbose_name="体力", default=5)
    armor = models.IntegerField(verbose_name="护甲", default=0)
    lucky = models.IntegerField(default=1, verbose_name="幸运")
    charm = models.IntegerField(default=3, verbose_name="魅力")
    user_status = models.BooleanField(default=True, verbose_name="用户状态，用在用户注销的时候")

    def __str__(self):
        return self.user_id.nickname
