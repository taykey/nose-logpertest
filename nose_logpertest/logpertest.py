__author__ = 'roy'

import os
import logging
from logging import FileHandler
import time

from nose.plugins.base import Plugin


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

        # check or create the directory of the current test context exist
        dir_path = os.path.join(self.logs_run_dir, str(test.context))
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # add a file handler to write to the the test log file
        test.log_handler = FileHandler(os.path.join(dir_path, str(test)))
        log.addHandler(test.log_handler)

    def afterTest(self, test):
        log = logging.getLogger()
        log.removeHandler(test.log_handler)
