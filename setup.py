from setuptools import setup, find_packages

setup(name = "pylein",
      version = "0.1",
      description = "Setup python projects painlessly",
      url = "https://github.com/harshadss/pylein",
      author = "Harshad Saykhedkar",
      license = "BSD 3-Clause License",
      packages = find_packages(),
      test_suite = "nose.collector",
      tests_require = ['nose'],
      entry_points = {
        "console_scripts": ['pylein-run = pylein.__main__:main']
       } )
