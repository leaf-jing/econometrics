#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 00:05:19 2016

@author: lifujing
"""


import numpy as np, numpy.linalg as npl
import logging as log
# in python 3, we need .xxx instead of xxx to import module in the same dir
from .utils import lazyproperty   

logger = log.getLogger(__name__)

class LSModel:
    """
    ls model 
    """
    
    def __init__(self, x: np.ndarray , y: np.ndarray, autoconstant: bool = True):
        # note: [1,2,3] give a shape (3,). And [1,2,3]' gives (3,1)
        if x.ndim ==1 :
            r,c = 1, x.size
        r,c = x.shape
        # add the constant column
        if not (x[:,0]==1).all() and autoconstant:
            self._x = np.hstack((np.ones(r).reshape(r,1) , x))
            logger.info("The adjusted x matrix by padding ones")
        else:
            self._x = x    
        self._y = y

       
    @lazyproperty    
    def beta(self) -> np.ndarray:
        """
        inv(X'X)X'y
        """
        logger.info("Beta is computed...")
        return npl.pinv(self._x.T.dot(self._x)).dot(self._x.T).dot(self._y) 

    @lazyproperty        
    def residualmaker(self) -> np.ndarray:
        """
        residual can be obtained via e=y-Xb=(I-X((X'X)^-1)X')y=My
        """
        (r,c) = self._x.shape
        return np.eye(r) - self.projectionmat
    
    @lazyproperty
    def residauls(self) -> np.ndarray:
        """
        residaul = My
        """
        return self.residualmaker.dot(self._y)

    # projection matrix
    @lazyproperty
    def projectionmat(self) -> np.ndarray:
        """
        P = X'((X'X)^-1)X
        M = I-P
        Py=y_par
        
        """
        return self._x.dot(npl.pinv(self._x.T.dot(self._x))).dot(self._x.T)
        
    """
    SST = SSR + SSE
        
    """
    
    #Matrix M0
    @lazyproperty
    def shitmat(n):
        np.eye(n) - np.ones((n,n))/n
    
    #Total sum of squares
    @lazyproperty    
    def sst(self):
        # y'*M0*y or sum((y-y_bar)^2)
        y_bar = np.average(self._y)
        return np.sum((self._y-y_bar)**2)
    
    #Sum of squares due to regression
    @lazyproperty
    def ssr(self):
        x_bar = np.average(self._x,0) 
        return np.sum( ((self._x - x_bar).dot(self.beta)) ** 2)
        
    #Sum of squares due to error
    @lazyproperty
    def sse (self):
        return self.sst-self.ssr
        
    @lazyproperty    
    def r_sqaure(self):
        # 1 - (sse/sst) 
        return self.ssr/self.sst
         
    @lazyproperty    
    def r_sqaure_adj(self):
        (n,k) = self._x.shape 
        return 1 - (self.sse/(n-k))/(self.sst/(n-1))        