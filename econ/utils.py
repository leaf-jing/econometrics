#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 00:15:23 2016

@author: ljing
"""

def lazyproperty(fn):
    """
    a simple lazy property decorator. 
    """
    attr_name = '_lazy_' + fn.__name__
    
    #a read only prop...
    @property
    def _lazyproperty(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    
    return _lazyproperty