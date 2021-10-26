#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.postgres.fields import IntegerRangeField

from robot.models.base_class import BaseModel


class EqType(BaseModel):
    """装备类型"""
    name = models.CharField(verbose_name="名称", max_length=32, unique=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "装备类型"
        verbose_name_plural = verbose_name


class EqModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name="名字")
    description = models.CharField(max_length=255, verbose_name="描述")
    eq_type = models.ForeignKey(
        to=EqType,
        verbose_name="装备类型",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="eq_type_name"
    )
    attack = IntegerRangeField(verbose_name="攻击力加成")
    defense = IntegerRangeField(verbose_name="防御力加成")
    health_point = IntegerRangeField(verbose_name="生命值加成")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "装备"
        verbose_name_plural = verbose_name

