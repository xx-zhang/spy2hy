#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
author : actanble
date   : 2018年2月5日13:37:54
role   : 运维日志
'''

import logging
import os
import sys
import datetime

from .config import WIN_LOG_DIR, LINUX_LOG_DIR

DATE_FORMATER = str(datetime.datetime.now().date())
logpath = lambda log_flag: os.path.join(WIN_LOG_DIR, log_flag + ".log-" + DATE_FORMATER) \
    if sys.platform == 'win32' else os.path.join(LINUX_LOG_DIR, log_flag + ".log-" + DATE_FORMATER)


# 写日志类
class Log:

    def __init__(self, log_flag='ops'):
        self.logFlag = log_flag
        self.logFile = logpath(log_flag)

    def write_log(self, log_level='info', log_message=DATE_FORMATER):
        # 创建一个logger
        logger = logging.getLogger(self.logFlag)
        logger.setLevel(logging.DEBUG)

        # 建立日志目录
        log_dir = os.path.dirname(self.logFile)
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)

        # 创建一个handler用于写入日志文件
        fh = logging.FileHandler(self.logFile)
        fh.setLevel(logging.DEBUG)

        # 创建一个handler用于输出到终端
        th = logging.StreamHandler()
        th.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s')
        fh.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(th)

        # 记录日志
        level_dic = {'debug': logger.debug,
                     'info': logger.info,
                     'warning': logger.warning,
                     'error': logger.error,
                     'critical': logger.critical}
        level_dic[log_level](log_message)

        # 删除重复记录
        fh.flush()
        logger.removeHandler(fh)

        th.flush()
        logger.removeHandler(th)

    def info(self, message):
        return self.write_log('info', message)

    def warn(self, message):
        return self.write_log('warning', message)

    def error(self, message):
        return self.write_log('error', message)

    def critical(self, message):
        return self.write_log('critical', message)

    def debug(self, message):
        return self.write_log('debug', message)


if __name__ == "__main__":
    pass