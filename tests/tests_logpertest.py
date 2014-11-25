__author__ = 'roy'

import os
import logging

logger = logging.getLogger()


class TestA():

    _multiprocess_can_split_ = True

    def setup(self):
        logger.info("im in setup")

    def teardown(self):
        logger.info("im in teardown")

    def test1(self):
        logger.info("I'm in test1")
        assert 1 == 1

    def test2(self):
        logger.info("I'm in test2")
        logger.info(os.getpid())
        assert 5 == 5

    def test3(self):
        logger.info("I'm in test3")
        logger.info(os.getpid())
        assert 5 == 5

    def test4(self):
        logger.info("I'm in test4")
        logger.info(os.getpid())
        assert 5 == 5


class TestB():

    _multiprocess_can_split_ = True

    def setup(self):
        logger.info("im in setup")

    def teardown(self):
        logger.info("im in teardown")

    def test1(self):
        logger.info("I'm in test1")
        logger.info(os.getpid())
        assert 1 == 1

    def test2(self):
        logger.info("I'm in test2")
        logger.info(os.getpid())
        assert 5 == 5

    def test3(self):
        logger.info("I'm in test3")
        logger.info(os.getpid())
        assert 5 == 5

    def test4(self):
        logger.info("I'm in test4")
        logger.info(os.getpid())
        assert 5 == 5



