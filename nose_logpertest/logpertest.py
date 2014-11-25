__author__ = 'roy'

from nose.plugins.base import Plugin
import os
import logging
from logging import FileHandler
import time

log = logging.getLogger()

logs_run_dir = time.strftime("%Y%m%d-%H%M%S")


class LogPerTest(Plugin):

    name = 'logpertest'

    def options(self, parser, env=os.environ):
        super(LogPerTest, self).options(parser, env=env)

    def configure(self, options, conf):
        super(LogPerTest, self).configure(options, conf)
        if not self.enabled:
            return
        self.logs_run_dir = logs_run_dir
        if not os.path.exists(self.logs_run_dir):
            os.makedirs(self.logs_run_dir)

    def beforeTest(self, test):
        log = logging.getLogger()
        if not os.path.exists(self.logs_run_dir + '/' + str(test.test.context)):
            os.makedirs(self.logs_run_dir + '/' + str(test.test.context))
        test.log_handler = FileHandler(self.logs_run_dir + '/' +
                                       str(test.test.context) + '/' + str(test))
        log.addHandler(test.log_handler)

    def afterTest(self, test):
        log.removeHandler(test.log_handler)
