# -*- coding:utf-8 -*-
"""
@Author : Puppet
@Lang : Python
@File : logger.py
@Kind : Script or Tool
@Desc : 简易日志记录
@System : Windows 10
@Data : 2022年06月23日
"""

import logging
from logging import handlers

import datetime


def get_logger():
    """
       初始化Log,创建Log
    """
    logger = logging.getLogger('log')
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        sh = logging.StreamHandler()
        fmt = logging.Formatter(fmt='[%(name)s] - %(asctime)s - %(levelname)s - %(message)s')
        sh.setFormatter(fmt)
        sh.setLevel(logging.DEBUG)
        logger.addHandler(sh)
        NowDay = datetime.date.today()
        filename = str(NowDay) + '.log'
        th = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=100, encoding='utf-8')
        th.setFormatter(fmt=fmt)  # 设置文件里写入的格式
        logger.addHandler(th)
    return logger


class Log:
    """
       实例化Log,静态调用
    """

    logger = get_logger()

    @staticmethod
    def debug(msg):
        Log.logger.debug(str(msg))

    @staticmethod
    def info(msg):
        Log.logger.info(str(msg))

    @staticmethod
    def error(msg):
        Log.logger.error(str(msg))

    @staticmethod
    def critical(msg):
        Log.logger.critical(str(msg))
