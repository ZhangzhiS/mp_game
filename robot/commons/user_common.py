#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from robot.models import User, UserProfile


def get_user_obj(openid) -> (Optional[User], Optional[UserProfile]):
    user = None
    try:
        user = User.objects.get(openid=openid, status=True)
        user_profile = UserProfile.objects.get(user_id=user.id, openid=openid)
    except User.DoesNotExist:
        return None, None
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(
            user_id=user.id,
            openid=openid
        )
        user_profile = UserProfile.objects.get(user_id=user.id, openid=openid)
    return user, user_profile
