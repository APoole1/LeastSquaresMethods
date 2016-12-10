"""
Module containing functions for the Newton algorithm, following the instructions at 'https://en.wikipedia.org/wiki/Newton's_method_in_optimization' (this link may not work, so copy it into search bar.
The algorithm here is used to minimise the least squares equation (https://en.wikipedia.org/wiki/Least_squares).
"""

import numpy
import matplotlib.pyplot as plt

import Functions

"""
Calculates the errors for each (x, y) pair, using the current estimate of the constants
"""
def GetRVector(f, xs, ys, consts):
    arr = [y - f(x, consts) for (x, y) in zip(xs, ys)]
    return numpy.matrix(arr).T

"""
Calculates the value of each derivative with the current estimate for the constants
"""
def FChange(f, diffs, xs, ys, consts):
    arr = []
    for d in diffs:
        sum = 0
        for (x, y) in zip(xs, ys):
            sum -= d(x, consts)*(y - f(x, consts))
        arr.append(sum*2)

    return numpy.matrix(arr).T

"""
Used to create the Hessian matrix. This works by using the 1st and 2nd derivatives of f to compute the 2nd derivatives of sum((y-f(x))^2)
"""
def GetHessian(f, diffs1, diffs2, xs, ys, consts):
    arr = []
    for (ds, d1) in zip(diffs2, diffs1):
        arrInner = []
        for (dd, d2) in zip(ds, diffs1):
            sum = 0
            for (x, y) in zip(xs, ys):
                sum -= dd(x, consts)*(y - f(x, consts))
                sum += d1(x, consts)*d2(x, consts)
            arrInner.append(sum*2)
        arr.append(arrInner)
    return numpy.matrix(arr)

"""
Calculates the next estimate for the constants, based on the current estimate
"""
def GetNextConsts(f, diffs1, diffs2, xs, ys, consts):
    fC =FChange(f, diffs1, xs, ys, consts)
    Hess = GetHessian(f, diffs1, diffs2, xs, ys, consts)
    Hess = Hess.I
    nextConstsVector = (numpy.matrix(consts).T - (Hess*fC))
    return numpy.squeeze(numpy.asarray(nextConstsVector))

"""
Calculates the co-efficient of determination from the rVec and sTot. The reason I used these inputs is because the will already be calculated in
the 'Run' method.
"""
def GetCoD(rVec, sTot):
    rVec = numpy.squeeze(numpy.asarray(rVec))
    sRes = 0.
    for i in rVec:
        sRes += i*i
    return (1-(sRes/sTot))

"""
Method to run the Newton algorithm, taking in the function to approximate and the data values. It returns a tuple of the 
constants for the function and the co-efficient of determination
"""
def Run(func, xs, ys, initial = None, iterations= 10, precision=0.01):
    f = func.f
    diffs1 = func.fs
    diffs2 = func.fs2

    # If no initial value is specified, use the default contained in func
    if initial is None:
        initial = func.initial

    # Calculate sTot at the start, as it will not change
    yMean = numpy.mean(ys)
    sTot = 0.
    for i in ys:
        sTot += ((i - yMean)**2)

    prevCoD = 0
    CoD = 0
    success = False

    rVec = GetRVector(f, xs, ys, initial)
    for i in range(0, iterations):
        initial = GetNextConsts(f, diffs1, diffs2, xs, ys, initial)
        rVec = GetRVector(f, xs, ys, initial)

        CoD = GetCoD(rVec, sTot)

        if (numpy.abs(CoD - prevCoD) < precision):
            success = True
            break

        prevCoD = CoD

    # If the co-efficient does not converge in time, let the user know
    if not success:
        print("Newton Method failed to converge")
        return None, None

    return (initial, CoD)