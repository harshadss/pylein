""" Setup the main structure of the project, tests and setup directory """

import os
import logging
from distutils.dir_util import mkpath
import distutils.errors

import pylein.templates as templates

LOGGER = logging.getLogger(__name__)

def setup_base_dirs(config):
    """ Create the basic directory of the project """
    working_dir = os.getcwd()
    base_dir = os.path.join(working_dir, config.name)
    proj_dir = os.path.join(base_dir, config.name)
    try:
        mkpath(proj_dir)
        return (base_dir, proj_dir)
    except distutils.errors.DistUtilsFileError, err:
        LOGGER.error("Problem while creating base dir:\n {}".format(err))

def setup_init_files(proj_dir):
    """ Setup empty init file """
    file_path = os.path.join(proj_dir, '__init__.py')
    open(file_path, 'w').close()

def setup_aux_files(base_dir):
    readme_file_path = os.path.join(base_dir, 'README.rst')
    # Add a dummy content to readme.
    with open(readme_file_path, 'w') as readmef:
        readmef.write(templates.get_readme_content())
    manifests_file_path = os.path.join(base_dir, 'MANIFEST.in')
    with open(manifests_file_path, 'w') as manifestf:
        manifestf.write(templates.get_manifest_content())
    
def setup_tests(config):
    """ Setup tests directory with a failing test. This function hides
        the implementation detail of where the test directory is created"""
    working_dir = os.getcwd()
    base_dir = os.path.join(working_dir, config.name)
    proj_dir = os.path.join(base_dir, config.name)
    test_dir = os.path.join(proj_dir, 'tests')
    try:
        mkpath(test_dir)
    except distutils.errors.DistUtilsFileError, err:
        LOGGER.error("Problem while creating test dir:\n {}".format(err))
    # Now create a test file and add a basic failing test to it.
    test_file_path = os.path.join(test_dir, '__init__.py')
    with open(test_file_path, 'w') as testf:
        testf.write(templates.get_test_code())

def create(config):
    """ Setting up main project structure and copy over
        basic file templates.
        Config is command line arguments passed"""
    base_dir, proj_dir = setup_base_dirs(config)
    setup_init_files(proj_dir)
    if config.test:
        setup_tests(config)

    if config.template == 'app':
        # In case of apps, we would want to create command line script
        # As a contract, we create a command line script of name projectname-run
        # First create a main file
        main_file_path = os.path.join(proj_dir, '__main__.py')
        # Write data to this file from template
        with open(main_file_path, 'w') as mainf:
            mainf.write(templates.get_main_code(config.template))

    # Setup file
    setup_file_path = os.path.join(base_dir, 'setup.py')
    setup_code = templates.get_setup_code(config.name,
                                          config.template)
    with open(setup_file_path, 'w') as setupf:
        setupf.write(setup_code)

    # Add auxillary files like README and manifests
    setup_aux_files(base_dir)
    
