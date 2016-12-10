Least-Squares Methods
======================

This Python project is used to automatically fit lines and curves of best fit to experimental data.

Installation
-------------

To run this project, you will need:

- Python 3.x
- Numpy
- Matplotlib

The project is just a collection of modules that can be imported as normal.

Features
-------- 

- The project contains implementations of 2 algorithms: The Newton Algorithm and the Gauss Newton Algorithm.

- The main file for the project is "LeastSquaresMethods.py". This contains an important function called "RunAndPlot", that will calculate constants and plot the result for a given function and set of data.
  You can specify which algorithm to use with the 'method' parameter (e.g. "method = 'GN'"), and the initial estimate with the 'initial' parameter. You can also specify how many iterations to do and the degree of accuracy.
  The function will return the approximation for the constants and the co-efficient of determination.
  
- You can run Gauss-Newton or Newton algorithms without plotting. To do this with Newton, import the Newton.py file and use "Newton.Run(<data>)". It is the same for Gauss-Newton, except using a different file.

- There is one more file, "Functions.py", that includes a set of sample functions to run the algorithms on. It also contains a class, "Func", that allows the user to specify their own functions. Please read the comments in
  the file for more information on how to use this
  
- The file "LeastSquaresMethods.py" also contains a function, "TimeFunctions", that is used to compare the speeds of the 2 algorithms on a given function, using random data. Based on my tests, Gauss-Newton is significantly
  faster
  
To-do
-----

- Add a function to run the algorithms with a range of functions, to determine which one fits best

- Add more sample functions

- Make the program able to deduce a good initial attempt, rather than having it fixed or entered by the user

- Potentially implement Levenberg-Marquadt algorithm

Support
-------

If you are having issues, contact me at anthony.poole@oriel.ox.ac.uk