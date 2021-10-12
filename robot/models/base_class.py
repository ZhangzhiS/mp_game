#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from django.db import models


class BaseModel(models.Model):

    class Meta:
        abstract = True

    def to_dict(self, exclude=None) -> dict:
        if exclude is None:
            exclude = {}
        res = dict()
        for k, v in self.__dict__.items():
            if k in exclude or k == "_state":
                continue
            if isinstance(getattr(self, k), datetime.datetime):
                res[k] = v.strftime("%Y-%m-%d %H:%M:%S")
            else:
                res[k] = v
        return res
