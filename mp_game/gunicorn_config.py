# -*- coding: utf-8 -*-
import multiprocessing


bind = '0.0.0.0:8001'
workers = multiprocessing.cpu_count()

backlog = 2048
daemon = False
debug = False
keepalive = 120
timeout = 120
proc_name = 'mp_game'
errorlog = '-'
accesslog = '-'
loglevel = 'info'
access_log_format = '%(h)s %(t)s %(r)s %(q)s'
