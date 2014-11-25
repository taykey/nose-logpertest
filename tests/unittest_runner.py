__author__ = 'roy'

import os
import glob
import shutil
import unittest

from nose import run
from nose_logpertest.logpertest import LogPerTest

from config import A_DIR_PATH, B_DIR_PATH, EXPECTED_A, EXPECTED_B


class TestLogPerTest(unittest.TestCase):

    def setUp(self):
        remove_unneeded_log_dirs()
        # run nose tests
        run(argv=['nosetests', '--with-logpertest'],
            addplugins=[LogPerTest()])

    def tearDown(self):
        remove_unneeded_log_dirs()

    def test_file_per_test(self):

        # get all the log files that were created by the nose run
        log_files_a = [os.path.basename(file) for file in
                       glob.glob(A_DIR_PATH + '/*')]

        log_files_b = [os.path.basename(file) for file in
                       glob.glob(B_DIR_PATH + '/*')]

        # assert the files that were created suits the expected files
        assert sorted(log_files_a) == sorted(EXPECTED_A)
        assert sorted(log_files_b) == sorted(EXPECTED_B)


def remove_unneeded_log_dirs():
    """remove directories that contain the log files"""
    for dir in glob.glob(A_DIR_PATH):
        shutil.rmtree(dir)
    for dir in glob.glob(B_DIR_PATH):
        shutil.rmtree(dir)

    # delete empty dirs
    for empty_dir in glob.glob('./*/'):
        os.rmdir(empty_dir)


if __name__ == '__main__':
    unittest.main()