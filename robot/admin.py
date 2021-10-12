#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from robot import models


class LevelConfigAdmin(admin.ModelAdmin):
    pass


class BodyLevelConfigAdmin(admin.ModelAdmin):
    pass


class PlayerAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.LevelConfig, LevelConfigAdmin)
admin.site.register(models.BodyLevelConfig, BodyLevelConfigAdmin)
admin.site.register(models.UserProfile, PlayerAdmin)
