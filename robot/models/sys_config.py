#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class LevelConfig(models.Model):
    """等级相关配置"""
    level = models.IntegerField(default=0, help_text="等级")
    level_label = models.CharField(max_length=100, help_text="等级展示")
    consume_exp = models.BigIntegerField(default=0, help_text="消耗经验")
    body_level_limit = models.IntegerField(default=1, help_text="肉身等级需求")
    exp_ampl = models.IntegerField(default=5, help_text="修为加成")
    status = models.BooleanField(default=True)


class BodyLevelConfig(models.Model):
    """肉身等级相关配置"""
    level = models.IntegerField(default=0, help_text="等级")
    level_label = models.CharField(max_length=100, help_text="等级展示")
    consume_exp = models.BigIntegerField(default=0, help_text="消耗经验")
    exp_level_limit = models.IntegerField(default=0, help_text="境界等级限制")
    status = models.BooleanField(default=True)
