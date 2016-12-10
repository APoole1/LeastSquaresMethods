"""
Module containing functions for the Gauss-Newton algorithm, following the instructions at https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm
"""


import numpy
import matplotlib.pyplot as plt

import Functions

"""
Builds and returns the Jacobian matrix, using the derivatives specified by the user
"""
def GetJacobian(fs, xs, consts):
    arr = []
    for x in xs:
        row = []
        for f in fs:
            row.append((-1)*f(x, consts))
        arr.append(row)
    return numpy.matrix(arr)

"""
Calculates the errors for each (x, y) pair, using the current estimate of the constants
"""
def GetRVector(f, xs, ys, consts):
    arr = [y - f(x, consts) for (x, y) in zip(xs, ys)]
    # convert to column-vector
    return numpy.matrix(arr).T

"""
Calculates the next estimate for the constants, based on the current estimate
"""
def GetNextConsts(f, fs, xs, consts, rVec = None):
    if rVec is None:
        rVec = GetRVector(f, xs, ys, consts)

    J = GetJacobian(fs, xs, consts)
    constVec = numpy.matrix(consts).T
    temp = J.T*J
    while True:
        try:
            temp = temp.I
            break
        except:
            print("SINGULAR")
            temp = temp + (numpy.eye(temp.shape[0])*(10^-5))

    print("")
    nextConsts = constVec - temp*J.T*rVec

    return numpy.squeeze(numpy.asarray(nextConsts))

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
Method to run the Gauss-Newton algorithm, taking in the function to approximate and the data values. It returns a tuple of the 
constants for the function and the co-efficient of determination
"""
def Run(func, xs, ys, initial = None, iterations= 10, precision=0.01):

    # The second derivative is not needed for this method, so only extract f and fs
    f = func.f
    derivatives = func.fs

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
        initial = GetNextConsts(f, derivatives, xs, initial, rVec)
        rVec = GetRVector(f, xs, ys, initial)

        CoD = GetCoD(rVec, sTot)

        if (numpy.abs(CoD - prevCoD) < precision):
            success = True
            break

        prevCoD = CoD

    # If the co-efficient does not converge in time, let the user know
    if not success:
        print("Guass Newton Method failed to converge. Try altering the initial estimate, increasing the number of iterations or lowering the precision")
        return None, None

    return initial, CoD