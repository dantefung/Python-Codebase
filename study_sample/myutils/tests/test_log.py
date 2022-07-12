'''
@Description:
@Author: jorian
@Date: 2020-06-25 01:57:44
'''
from study_sample.myutils.log_util import logFactory

log = logFactory("test").log


def test():
    log.info("test log info")
    log.debug("test log debug")
    log.error("test log error")
    log.warning("test log warn")
    arr = [1, 2, 3, 4]
    log.info(arr)
    log.info('>>>>>%s', arr)
    di = {'a': 22}
    log.info('>>>>>%s %s', arr, di)
    # 错误用法：  log.info('aaa', 'bbb')


if __name__ == '__main__':
    test()
