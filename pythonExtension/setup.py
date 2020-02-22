# https://docs.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2019

from distutils.core import setup, Extension, DEBUG

sfc_module = Extension('pythonExtension', sources = ['module.cpp'])

setup(name = 'pythonExtension', version = '1.0',
    description = 'Python Package with superfastcode C++ extension',
    ext_modules = [sfc_module]
    )
