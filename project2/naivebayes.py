#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Heming
"""

import numpy as np
from naivebayesPY import naivebayesPY
from naivebayesPXY import naivebayesPXY

def naivebayes(x, y, x1):
# =============================================================================
#function logratio = naivebayes(x,y,x1);
#
#Computation of log P(Y|X=x1) using Bayes Rule
#Input:
#x : n input vectors of d dimensions (dxn)
#y : n labels (-1 or +1)
#x1: input vector of d dimensions (dx1)
#
#Output:
#logratio: log (P(Y = 1|X=x1)/P(Y=-1|X=x1))
# =============================================================================

    # Convertng input matrix x and x1 into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    X = np.matrix(x)
    X1= np.matrix(x1)
    
    # Pre-configuring the size of matrix X
    d,n = X.shape
    
# =============================================================================
# fill in code here

    pos, neg = naivebayesPY(x, y)
    posprob, negprob = naivebayesPXY(x, y)

    # get (P(Y = 1|X=x1)
    posprob_dot = np.zeros([d, 1])
    for i in range(d): 
        if x1[i, :] == 0:
            # posprob_dot[i, :] = (1 - posprob[i, :]) # categorical prod
            posprob_dot[i, :] = 1
        else:
            posprob_dot[i, :] = posprob[i, :]
    positive_prob = pos * np.prod(posprob_dot)

    # get (P(Y = -1|X=x1)
    negprob_dot = np.zeros([d, 1])
    for i in range(d): 
        if x1[i, :] == 0:
            # negprob_dot[i, :] = (1 - negprob[i, :]) # categorical prod
            negprob_dot[i, :] = 1
        else:
            negprob_dot[i, :] = negprob[i, :]
    negative_prob = neg * np.prod(negprob_dot)

    print(posprob_dot)
    print(negprob_dot)
    print(positive_prob)
    print(negative_prob)
    logratio = np.log(positive_prob / negative_prob)
    
    return logratio
# =============================================================================
