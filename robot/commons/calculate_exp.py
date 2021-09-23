#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import time

from mp_game.settings import MAX_STUDY_TIME


def get_add_exp(state_session):
    """修炼经验计算"""
    last_status = state_session.get("study_status", False)
    if not last_status:
        return 0
    now_time_step = int(time.time())
    add_exp = state_session["add_exp"]
    last_time_step = state_session.get("start_time")
    surplus_time = state_session.get("surplus_time", 0)
    time_more_than = now_time_step - last_time_step
    forever_study = state_session.get("forever_study", False)
    if not forever_study:
        if time_more_than > MAX_STUDY_TIME:
            if surplus_time:
                exp = surplus_time // 5 * add_exp
            else:
                exp = (MAX_STUDY_TIME // 5) * add_exp
            state_session["surplus_time"] = 0
        else:
            if surplus_time:
                new_study_time = time_more_than - (MAX_STUDY_TIME - surplus_time)
                exp = new_study_time // 5 * add_exp
                new_surplus_time = surplus_time - new_study_time + (new_study_time % 5)
            else:
                exp = (time_more_than // 5) * add_exp
                new_surplus_time = MAX_STUDY_TIME - time_more_than + (time_more_than % 5)
            state_session["surplus_time"] = new_surplus_time
    else:
        state_session["start_time"] = now_time_step - (time_more_than % 5)
        exp = (time_more_than // 5) * add_exp
    return exp
