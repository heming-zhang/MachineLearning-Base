#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Heming
"""

import numpy as np

def naivebayesPXY(x, y):
# =============================================================================
#    function [posprob,negprob] = naivebayesPXY(x,y);
#
#    Computation of P(X|Y)
#    Input:
#    x : n input vectors of d dimensions (dxn)
#    y : n labels (-1 or +1) (1xn)
#    
#    Output:
#    posprob: probability vector of p(x|y=1) (dx1)
#    negprob: probability vector of p(x|y=-1) (dx1)
# =============================================================================


    
    # Convertng input matrix x and y into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    X = np.matrix(x)
    Y = np.matrix(y)
    
    # Pre-configuring the size of matrix X
    d,n = X.shape
    
    # Pre-constructing a matrix of all-ones (dx2)
    X0 = np.ones((d,2))
    Y0 = np.matrix('-1, 1')
    
    # add one all-ones positive and negative example
    Xnew = np.hstack((X, X0)) #stack arrays in sequence horizontally (column-wise)
    # Xnew = np.concatenate((X, X0), axis=1) #concatenate to column
    Ynew = np.hstack((Y, Y0))
    
    # Re-configuring the size of matrix Xnew
    d,n = Xnew.shape
    
# =============================================================================
# fill in code here

    # (1) First condition for y = +1
    # calculate the each dimensions d_alpha occurrences
    indicator_dim = np.zeros([d, 1])
    for alpha in range(d):
        for i in range(n):
            if Ynew[:, i] == 1: 
                indicator_dim[alpha, :] += Xnew[alpha, i]
    # also the sum of all features value with y = +1
    feature_sum = 0
    point_sum = np.sum(Xnew, axis = 0)
    for i in range(n):
        if Ynew[:, i] == 1:
            feature_sum += point_sum[:, i]
    posprob = indicator_dim / feature_sum
    
    # denom = np.sum(Ynew ==1)
    # posprob = indicator_dim / denom

    # (2) Second condition for y = -1
    # calculate the each dimensions d_alpha occurrences
    indicator_dim = np.zeros([d, 1])
    for alpha in range(d):
        for i in range(n):
            if Ynew[:, i] == -1: 
                indicator_dim[alpha, :] += Xnew[alpha, i]
    # also the sum of all features value with y = +1
    feature_sum = 0
    point_sum = np.sum(Xnew, axis = 0)
    for i in range(n):
        if Ynew[:, i] == -1:
            feature_sum += point_sum[:, i]
    negprob = indicator_dim / feature_sum

    return posprob, negprob

# =============================================================================
