#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 15:06:43 2016

@author: lifujing
"""

import os
import logging.config
import yaml

"""should be only called once in the main entrance !!!"""
def setup_logging(default_path='log.yaml', 
                  default_level=logging.INFO, 
                  env_key='LOG_CFG'):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        print("!!! no config found !!!")
        logging.basicConfig(level=default_level)



