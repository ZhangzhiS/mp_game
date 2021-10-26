#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
计算修炼经验
"""
import random
import time

from mp_game.settings import MAX_STUDY_TIME


def range_calculator(c_time, add_exp):
    exp = 0
    count = c_time // 5
    if count > 30:
        exp = count * add_exp
        return exp
    for i in range(c_time//5):
        exp += random.randint(add_exp-3, add_exp+3)
    return exp


def get_add_exp(state_session):
    """修炼经验计算"""
    last_status = state_session.get("study_status", False)
    if not last_status:
        return 0
    now_time_step = int(time.time())
    add_exp = state_session.get("exp_add", 5)
    last_time_step = state_session.get("start_time")
    surplus_time = state_session.get("surplus_time", 0)
    time_more_than = now_time_step - last_time_step
    if time_more_than < 5:
        return 0
    forever_study = state_session.get("forever_study", False)
    if not forever_study:
        if time_more_than > MAX_STUDY_TIME:
            if surplus_time:
                exp = range_calculator(surplus_time, add_exp)
            else:
                exp = range_calculator(MAX_STUDY_TIME, add_exp)
            state_session["surplus_time"] = 0
            state_session["study_status"] = False
        else:
            if surplus_time:
                new_study_time = time_more_than - (MAX_STUDY_TIME - surplus_time)
                exp = range_calculator(new_study_time, add_exp)
                new_surplus_time = surplus_time - new_study_time + (new_study_time % 5)
            else:
                exp = range_calculator(time_more_than, add_exp)
                new_surplus_time = MAX_STUDY_TIME - time_more_than + (time_more_than % 5)
            state_session["surplus_time"] = new_surplus_time
    else:
        state_session["start_time"] = now_time_step - (time_more_than % 5)
        exp = range_calculator(time_more_than, add_exp)
    return exp
