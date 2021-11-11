#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from django.core.management import BaseCommand
from robot.models.sys_config import LevelConfig


class Command(BaseCommand):
    help = '修改公众号菜单'

    def handle(self, *args, **options):
        a = 13469199089641601294165159418313264309149074316066816
        print(a)
        print(type(a))
        t = 0
        with open("level.csv", "r") as f:
            level_num = 1
            tmp_exp = random.randint(6, 9)
            for i in f:
                i = i.split()[0]
                level_list = [
                    "1阶",
                    "2阶",
                    "3阶",
                    "4阶",
                    "5阶",
                    "6阶",
                    "7阶",
                    "8阶",
                    "9阶",
                    "10阶",
                ]
                for level_lab in level_list:
                    exp = tmp_exp * 2
                    t += exp
                    tmp_exp = exp
                    lc = LevelConfig(
                        level=level_num,
                        level_label=i+level_lab,
                        consume_exp_range=(exp, exp + 10),
                        last_level=level_num-1
                    )
                    print(lc)
                    lc.save()
                    level_num += 1
