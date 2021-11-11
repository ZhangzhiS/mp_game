#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.postgres.fields import BigIntegerRangeField

from robot.models.base_class import BaseModel


class LevelConfig(BaseModel):
    """等级相关配置"""
    level = models.IntegerField(default=0, verbose_name="等级")
    level_label = models.CharField(max_length=100, verbose_name="等级展示")
    consume_exp_range = BigIntegerRangeField(verbose_name="消耗经验的随机范围", default=[1, 10])
    body_level_limit = models.IntegerField(default=1, verbose_name="肉身等级需求")
    exp_ampl = models.IntegerField(default=5, verbose_name="修为加成")
    last_level = models.IntegerField(default=0, verbose_name="上一等级")
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "修炼等级配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.level},{self.level_label},{self.consume_exp_range}"


class BodyLevelConfig(BaseModel):
    """肉身等级相关配置"""
    level = models.IntegerField(default=0, verbose_name="等级")
    level_label = models.CharField(max_length=100, verbose_name="等级展示")
    consume_exp_range = BigIntegerRangeField(verbose_name="消耗经验的随机范围", default=[1, 10])
    exp_level_limit = models.IntegerField(default=0, verbose_name="境界等级限制")
    is_exam = models.BooleanField(default=True, verbose_name="是否需要渡劫")
    default_exam_probability = models.IntegerField(verbose_name="默认渡劫成功率", default=80)
    last_level = models.IntegerField(default=0, verbose_name="上一等级")
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "肉身等级配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.level_label
