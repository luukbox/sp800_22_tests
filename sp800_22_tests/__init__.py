import os
import sys
import inspect


def test_sequence(seqpath):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    dirpath = os.path.dirname(os.path.abspath(filename))
    os.system(f'python {dirpath}{os.sep}sp800_22_tests.py {seqpath}')
