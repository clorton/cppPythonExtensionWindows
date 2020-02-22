# C++ Extension to Python in Windows (Visual Studio 2019)

A sample solution with two projects, Python and C++ to demonstrate building a C++ extension to Python in Windows.

Source: https://docs.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2019

## Instructions

1. Create a new solution with a Python application project.
2. Add new empty C++ project.
3. Add C++ code to C++ project.
4. In the C++ project properties, set the following:
* General > Target Name
* Advanced > Target Extension = ".pyd"
* General > Project Defaults > Configuration Type = "Dynamic Library (.dll)"
* C/C++ General > Additional Include Directories = *path to Python\include*
* C/C++ Preprocessor > Preprocessor Definitions += "Py_LIMITED_API;"
* C/C++ Code Generation > Runtime Library = Multi-threaded DLL (/MD) (also for debug)
* Linker > General > Additional Library Directories = *path to Python\libs* (not Lib)
