This plugin creates a log file per test run by nose,
holding the logs of that specific test

==========
Installing
==========

You can install `nose-logpertest` plugin using `pip`:

.. code-block:: shell

    $ pip install nose-logpertest


=====
Using
=====

Given the following tests:

.. code-block:: python

    class TestA():

        def test1(self):
            logger.info("I'm in test 1")
            assert 1 == 1

        def test2(self):
            logger.info("I'm in test 2")
            assert 2 == 2

        def test3(self):
            logger.info("I'm in test 3")
            assert 3 == 3


    class TestB():

        def test1(self):
            logger.info("I'm in test 1")
            assert 1 == 1

        def test2(self):
            logger.info("I'm in test 2")
            assert 2 == 2



running it with `nosetest` using `nose-logpertest` plugin:

.. code-block:: shell

    nosetests --with-logpertest

will cause the creation of the following log files:

.. code-block:: shell

    <20141125-120146>
        <TestA>
            test1
            test2
            test3
        <TestB>
            test1
            test2

where each file holds the logs of that specific test and `20141125-120146` is the running time of the tests

========
Authors
========

:Authors:
    Roy Klinger
:Contributors:
    Tal Ben Basat

    Nicole Franco

    Maroun Maroun

    Sergey Ragatsky
:Version: 0.0.1 of 27/11/2014




