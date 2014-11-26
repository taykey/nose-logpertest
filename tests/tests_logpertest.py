__author__ = 'roy'

import logging

logger = logging.getLogger()


class TestA():

    _multiprocess_can_split_ = True

    def setup(self):
        logger.info("im in setup")

    def teardown(self):
        logger.info("im in teardown")

    def test1(self):
        logger.info("im in test 1")
        assert 1 == 1

    def test2(self):
        logger.info("im in test 2")
        assert 2 == 2

    def test3(self):
        logger.info("im in test 3")
        assert 3 == 3

    def test4(self):
        logger.info("im in test 4")
        assert 4 == 4


class TestB():

    _multiprocess_can_split_ = True

    def setup(self):
        logger.info("im in setup")

    def teardown(self):
        logger.info("im in teardown")

    def test1(self):
        logger.info("im in test 1")
        assert 1 == 1

    def test2(self):
        logger.info("im in test 2")
        assert 2 == 2

    def test3(self):
        logger.info("im in test 3")
        assert 3 == 3

    def test4(self):
        logger.info("im in test 4")
        assert 4 == 4



