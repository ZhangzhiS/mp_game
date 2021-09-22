#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from werobot import WeRoBot
from mp_game.settings import WECHAT_SECRET, WECHAT_APPID

robot = WeRoBot()
robot.config["APP_ID"] = WECHAT_APPID
robot.config["APP_SECRET"] = WECHAT_SECRET
client = robot.client


class Command(BaseCommand):
    help = '修改公众号菜单'

    def handle(self, *args, **options):
        res = client.create_menu({
            "button": [
                {
                    "type": "click",
                    "name": "探索",
                    "key": "find"
                },
                {
                    "type": "click",
                    "name": "当前",
                    "key": "info"
                },
                {
                    "type": "click",
                    "name": "修炼",
                    "key": "study"
                },
                # {
                #     "name": "菜单",
                #     "sub_button": [
                #         {
                #             "type": "view",
                #             "name": "搜索",
                #             "url": "http://www.soso.com/"
                #         },
                #         {
                #             "type": "view",
                #             "name": "视频",
                #             "url": "http://v.qq.com/"
                #         },
                #         {
                #             "type": "click",
                #             "name": "赞一下我们",
                #             "key": "V1001_GOOD"
                #         }
                #     ]
                # }
            ]})
        self.stdout.write(self.style.SUCCESS(f"CreateMenu SUCCESS {res}"))
