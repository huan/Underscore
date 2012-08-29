#!/usr/bin/python

import nose.tools as nt
import glob
import traceback
import os.path
import underscore
import sys
import StringIO
import warnings

def testGenerator():
    for filename in glob.glob('examples/*.py'):
        yield _testFile, filename

def _testFile(original_file):
    underscored_file = os.path.join('examples', 'underscored', 
                               os.path.basename(original_file))
    expected_output = _execute(original_file)
    actual_output = _execute(underscored_file)
    nt.assert_equal(actual_output, expected_output)

def _execute(filename):
    sys.stdout = fileOut = StringIO.StringIO()
    with open(filename) as python_file:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            exec python_file.read() in {}
    sys.stdout = sys.__stdout__
    output = fileOut.getvalue()
    fileOut.close()
    return output
