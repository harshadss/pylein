"""Define code templates to be included in other files """
import pdb



APP_MAIN = """
import argparse

def parse_cmd_args():
    cmd = argparse.ArgumentParser(description="Write description here")
    cmd.add_argument('--arg', action = 'store',
                     help = "Add an argument")
    
def main():
    parse_cmd_args()

if __name__ == '__main__':
    main()    
"""

# Note that embedded curly braces should be handled carefully while using format

APP_SETUP = """
from setuptools import setup, find_packages

setup(name = "{0}",
      version = "0.1",
      description = "Write some description",
      url = "",
      author = "",
      license = "",
      packages = find_packages(),
      test_suite = "nose.collector",
      tests_require = ['nose'],
      entry_points = {{
        "console_scripts": ['{1} = {0}.__main__:main']
       }} )
"""

LIB_SETUP = """
from setuptools import setup, find_packages

setup(name = "{0}",
      version = "0.1",
      description = "Write some description",
      url = "",
      author = "",
      license = "",
      packages = ["{0}"],
      test_suite = "nose.collector",
      tests_require = ['nose'])
"""

TEST_SETUP = """
from unittest import TestCase

class FixMe(TestCase):
    def test_failing(self):
        self.assertEqual(1, 0)

"""

README_CONTENT = """
=====
Title
=====

Section 1
-----
This is section one.

Section 2
-----
This is section two. `Read more about rst files at
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_.

"""

MANIFEST_CONTENT = """
include README.rst
"""

def get_main_code(proj_type = "app"):
    return APP_MAIN

def get_setup_code(proj_name, proj_type = "app"):
    pdb.set_trace()
    if proj_type == "app":
        run_script_name = "{0}-run".format(proj_name)
        return APP_SETUP.format(proj_name, run_script_name)
    else:
        return LIB_SETUP.format(proj_name)

def get_test_code():
    """ Returns a dummy test code """
    return TEST_SETUP

def get_readme_content():
    return README_CONTENT

def get_manifest_content():
    return MANIFEST_CONTENT
