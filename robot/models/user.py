#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    """用户"""
    openid = models.CharField(max_length=255, help_text="用户的openid", db_index=True)
    nickname = models.CharField(max_length=32, help_text="用户的昵称")
    sub_time = models.DateTimeField(auto_created=True, auto_now_add=True, help_text="注册时间")
    gender = models.IntegerField(null=True, help_text="性别, 1:男，2:女")
    status = models.BooleanField(default=True, help_text="用户状态")


class UserProfile(models.Model):
    """用户属性"""
    user_id = models.IntegerField(help_text="用户的id")
    openid = models.CharField(max_length=255, help_text="用户的openid", db_index=True)
    level = models.IntegerField(help_text="境界", default=1)
    level_label = models.CharField(max_length=100, help_text="境界展示名称", default="筑基一阶")
    body_level = models.IntegerField(help_text="肉身", default=1)
    body_level_label = models.CharField(max_length=100, help_text="身体等级展示名称", default="铁骨一阶")
    exp = models.BigIntegerField(help_text="当前修为", default=0)
    exp_add = models.IntegerField(help_text="每秒修为增长数量", default=5)
    max_health_point = models.IntegerField(help_text="最大生命值", default=100)
    health_point = models.IntegerField(help_text="当前生命值", default=100)
    max_mana_point = models.IntegerField(help_text="最大法力值", default=100)
    mana_point = models.IntegerField(help_text="当前法力值", default=100)
    strength = models.IntegerField(help_text="力量", default=5)
    dexterity = models.IntegerField(help_text="敏捷", default=5)
    intelligence = models.IntegerField(help_text="智力", default=5)
    vitality = models.IntegerField(help_text="体力", default=5)
    armor = models.IntegerField(help_text="护甲", default=0)
    lucky = models.IntegerField(default=1, help_text="幸运")
    charm = models.IntegerField(default=3, help_text="魅力")
    user_status = models.BooleanField(default=True, help_text="用户状态，用在用户注销的时候")
