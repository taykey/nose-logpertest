__author__ = 'roy'

expected_test_name = 'tests.tests_logpertest.Test{}.test{}'

EXPECTED_A = [expected_test_name.format('A', '1'),
              expected_test_name.format('A', '2'),
              expected_test_name.format('A', '3'),
              expected_test_name.format('A', '4'),
              ]

EXPECTED_B = [expected_test_name.format('B', '1'),
              expected_test_name.format('B', '2'),
              expected_test_name.format('B', '3'),
              expected_test_name.format('B', '4'),
              ]

A_DIR_PATH = './*/tests.tests_logpertest.TestA/'
B_DIR_PATH = './*/tests.tests_logpertest.TestB/'


LINES = {0: "im in setup", 1: "im in test", 2: "im in teardown"}