"""log in 4 files"""

import logging
import os

log_lvl = logging.DEBUG


def get_wise_logger(formatter, path, name=''):
    log = logging.getLogger(name)
    log.setLevel(log_lvl)
    lvls = ['debug', 'info', 'warn', 'error']

    if not os.path.exists(path):
        os.makedirs(path)

    for lvl in lvls:
        logfile = os.path.join(path, '{}.log'.format(lvl.lower()))
        hdlr = logging.FileHandler(logfile)
        hdlr.setLevel(getattr(logging, lvl.upper()))
        hdlr.setFormatter(formatter)
        log.addHandler(hdlr)
    return log


def debug_log(rel_path='../log/debug'):
    path = os.path.join(os.path.dirname(__file__), rel_path)
    formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(message)s|%(filename)s-%(lineno)s')
    return get_wise_logger(formatter, path, 'debug')


def operate_log(rel_path='../log/operate'):
    path = os.path.join(os.path.dirname(__file__), rel_path)
    formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(message)s')
    return get_wise_logger(formatter, path, 'debug.operate')


if __name__ == '__main__':
    log = debug_log(rel_path='log/debug')
    log.error('test log')
    log.info('info log')

    log2 = operate_log(rel_path='log/operate')
    log2.error('operate error log')
    log2.info('operate info log')
