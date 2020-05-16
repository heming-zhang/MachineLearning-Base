"""
INPUT:	
xTr : dxn input vectors
yTr : 1xn input labels
alphas : dx1 vector of alphas generated from quadratic program solution of svm
bias : bias of classifier generated by recoverBias
ktype : type of kernel
kpar : parameter of kernel
compute

Output:
svmclassify : a classifier (svmclassify(xTe) defined in this function 
that returns the binary predictions on xTe)

Creates an svm classifierthat can make predictions on new test data
"""
import numpy as np
from computeK import computeK

def createsvmclassifier(xTr, yTr, alphas, bias, ktype, kpar):
    # classifier that returns all ones
    def svmclassify(xTe):
        # Use Kernal Version Classifier [alphas * y * kernel + bias]
        d, n = xTe.shape
        K = computeK(ktype, xTr, xTe, kpar)
        coff = yTr * alphas
        result = np.dot(coff.T, K) + bias
        pred = np.sign(result).T
        return pred

    return svmclassify
    
if __name__ == "__main__":
    n = 20
    d = 10
    xTr = np.ones((d, n))
    yTr = np.ones((n, 1))
    alphas = np.ones((n, 1))
    bias = 0.5
    ktype = 'rbf'
    P = 1
    svmclassify = createsvmclassifier(xTr, yTr, alphas, bias, ktype, P)
    