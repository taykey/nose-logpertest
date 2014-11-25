__author__ = 'roy'


def main():
    logger = logging.getLogger(__name__)
    logger.info("im in main")
    run(argv=['nosetests', '--processes=-1','--process-restartworker','--process-timeout=300', '--with-logpertest', '-s' ,'--with-xunitmp'])

if __name__ == '__main__':
    main()