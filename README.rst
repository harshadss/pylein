====
pylein
====

Motivation
-----
Python is a very easy language to get started with. You can start writing
useful Python scripts in very short time after first brush with the language.
A slight trouble comes after familiarity, when things get little serious. After
writing lot of scrappy scripts, you might think about writing an actual, bigger
project in Python. This forces you to think about a number of problems, like:

  1. How do I structure my project? Should I have an src directory that contains
     code?
  2. Where should I put my tests? How should I import the modules to be tested
     without having tests pollute namespace?
  3. How will I distribute my code? If I were to write a library that is to be
     installed on a different server for use, how should I package my code?
  
This project/application helps to make process of setting up a Python
project simpler by assuming some sane default answers to the above questions.
The ideas implemented in this code are taken from this wonderful `Python
packaging tutorial <https://python-packaging.readthedocs.io/>`_. This is nothing
novel but just an attempt to automate the usual boring stuff at the start of new
project.

There are tools in other languages `particularly lein for Clojure
<leiningen.org>`_ which make this process very smooth. This tool is a very
(incomplete)cattempt to recreate that magic. The idea is can a newcomer get
started to actual project work without studying too many things about setuptools
and other things.

Disclaimer
-----

This is a heavy work in progress. The code needs cleanup/fixes, better handling
of exception. I have pushed it just to test and end-to-end run of creating a
Python project structure. Cleanups/fixes will be done soon.

Installation & Usage
-----

Not yet pushed to central repositories like pypi. So you can do the following
sequence.

  1. Clone the git repository.
  2. Go the project directory
     
     .. code:: bash

     cd pylein
     
  3. Use pip to install this project

     .. code:: bash

     pip install .
     
  4. Once installed, the package creates a run script called pylein-run
     in your path. Use pylein-run command to create a new project.
  5. The help given in the tool can be accessed as follows,

     .. code:: bash

     <path-to-run-script>/pylein-run --help

  6. Currently, you need to specify template to use (lib/app) and name of the
     project. You can optionally provide --test flag to indicate if test
     directory should be created.

To Be Implemented
-----

The lein tool implements many more useful options beyond creating a project
structure like running tests, building the project into a single jar for
deployement, running a dependency check etc. Some of these can be implemented
here.
