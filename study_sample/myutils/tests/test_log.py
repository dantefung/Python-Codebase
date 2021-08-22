'''
@Description:
@Author: jorian
@Date: 2020-06-25 01:57:44
'''
from study_sample.myutils.log_util import logFactory

loggger = logFactory("test").log


def test():
    loggger.info("test log info")
    loggger.debug("test log debug")
    loggger.error("test log error")
    loggger.warning("test log warn")


if __name__ == '__main__':
    test()