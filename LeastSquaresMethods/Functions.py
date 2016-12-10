"""
Module containing a class called 'Func' that can be used to represent functions that can be passed to Newton.
The module also contains a series of sample functions
"""

import numpy

class Func:
    """
    Constructor for the Func class.
    The first argument should be a function that takes a value and a list of constants, and returns a result.
    E.g. f(x, c) = c[0]*x + c[1] would represent linear functions.

    The second argument should be a list of functions, the derivatives of f with regard to each constant. Ensure that the index of each derivative
    matches the index of the constant in the constants of f. So for the example use [df/dc[0], df/dc[1]] and not [df/dc[1], df/dc[0]]

    The third argument should be a 2d matrix of the second derivatives. Again, you should respect the order used before. So, for the example, use
    [[df/dc[0]dc[0], df/dc[0]dc[1]],
     [df/dc[1]dc[0], df/dc[1]dc[1]].

    The fourth argument is used to specify what the default initial value should be when the function is run through the algorithms
    """
    def __init__(self, f, fs, fs2, initial = []):
        self.f = f
        self.fs = fs
        self.fs2 = fs2

        self.initial = initial

"""
The following are all sample functions
"""
# Linear
f = lambda x, consts : (consts[0]*x) + consts[1]

fs = []
fs.append(lambda x, consts : x)
fs.append(lambda x, consts : 1)

fs2 = [[lambda x, consts : 0, lambda x, consts : 0], [lambda x, consts : 0, lambda x, consts : 0]]

LINEAR = Func(f, fs, fs2, [1, 1])

# Linear squared (linear with positive constants, used for testing)

f = lambda x, consts : (consts[0]*consts[0]*x) + (consts[1]*consts[1])

fs = []
fs.append(lambda x, consts : 2*consts[0]*x)
fs.append(lambda x, consts : 2*consts[1])

fs2 = []
fs2.append([lambda x, consts: 2*x, lambda x, consts: 0])
fs2.append([lambda x, consts: 0, lambda x, consts: 2])

LINEAR_SQUARED = Func(f, fs, fs2, [1, 1])

# Exponential

f = lambda x, consts : consts[0] * numpy.exp(consts[1]*x)

fs = []
fs.append(lambda x, consts :numpy.exp(consts[1]*x))
fs.append(lambda x, consts : consts[0]*x*numpy.exp(consts[1]*x))

fs2 = []
fs2.append([])
fs2.append([])
fs2[0].append(lambda x, consts : 0); fs2[0].append(lambda x, consts : x*numpy.exp(consts[1]*x))
fs2[1].append(lambda x, consts : x*numpy.exp(consts[1]*x)); fs2[1].append(lambda x, consts : x*x*numpy.exp(consts[1]*x))

EXPONENTIAL = Func(f, fs, fs2, [0.5, 0.2])

# Biology equation

f = lambda x, consts : (consts[0] * x)/(consts[1] + x)

fs = []
fs.append(lambda x, consts : (x)/(consts[1] + x))
fs.append(lambda x, consts : (-consts[0]*x)/((consts[1] + x)**2))

fs2 = [[], []]
fs2[0].append(lambda x, consts : 0); fs2[0].append(lambda x, consts : (-x)/((consts[1] + x)**2))
fs2[1].append(lambda x, consts : (-x)/((consts[1] + x)**2)); fs2[1].append(lambda x, consts : (2*consts[0]*x)/((consts[1] + x)**3))

BIOLOGY = Func(f, fs, fs2, [0.5, 0.5])

# Biology with linear factor
f = lambda x, consts : (consts[0] * x)/(consts[1] + x) + consts[2]*x + consts[3]

fs = []
fs.append(lambda x, consts : (x)/(consts[1] + x))
fs.append(lambda x, consts : (-consts[0]*x)/((consts[1] + x)**2))
fs.append(lambda x, consts : x)
fs.append(lambda x, consts : 1)

fs2 = [[], [], [], []]
fs2[0].append(lambda x, consts : 0); fs2[0].append(lambda x, consts : (-x)/((consts[1] + x)**2)); fs2[0].append(lambda x, consts: 0); fs2[0].append(lambda x, consts: 0);
fs2[1].append(lambda x, consts : (-x)/((consts[1] + x)**2)); fs2[1].append(lambda x, consts : (2*consts[0]*x)/((consts[1] + x)**3)); fs2[1].append(lambda x, consts: 0); fs2[1].append(lambda x, consts: 0);
fs2[2].append(lambda x, consts: 0); fs2[2].append(lambda x, consts: 0); fs2[2].append(lambda x, consts: 0); fs2[2].append(lambda x, consts: 0);
fs2[3].append(lambda x, consts: 0); fs2[3].append(lambda x, consts: 0); fs2[3].append(lambda x, consts: 0); fs2[3].append(lambda x, consts: 0);

BIOLOGY_WITH_LINEAR = Func(f, fs, fs2, [0.5, 0.5, 1., 1.])

# Quadratic
f = lambda x, consts : consts[0] * (x**2) + consts[1]*x + consts[2]
fs = []
fs.append(lambda x, consts : x*x)
fs.append(lambda x, consts : x)
fs.append(lambda x, consts : 1)

zero = lambda x, consts : 0
fs2 = [[zero, zero, zero], [zero, zero, zero], [zero, zero, zero]]

Quadratic = Func(f, fs, fs2, [1, 0, 0])