#!/usr/bin/python
from configparser import ConfigParser
import os

"""
1. 导入 ConfigParser
2. 实例化一个 ConfigParser对象
3. 构建配置文件路径
4. 读取配置文件
5. 定义读取配置函数

问题：为什么要用with语句去打开一个文件？
"""


class Config:

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    REPORT_DIR = os.path.join(BASE_DIR, "report")
    IMAGE_DIR = os.path.join(BASE_DIR, 'screenshort')
    CONFIG_PATH = os.path.join(BASE_DIR, 'config.ini')

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(self.CONFIG_PATH, encoding='utf-8')

    def get_email(self, option):
        """
        获取 邮箱 相关配置
        :param option:
        :return:
        """
        return self.cf.get("EMAIL", option)

    def get_db(self, option):
        """
        获取 DB 相关配置
        :param option:
        :return:
        """
        return self.cf.get("DB", option)

    def get_report(self, option):
        """
        获取 REPORT 相关配置
        :param option:
        :return:
        """
        return self.cf.get("REPORT", option)

    def get_appium(self, option):
        """
        获取 Appium 相关配置
        :param option:
        :return:
        """
        return self.cf.get("APPIUM", option)


config = Config()


if __name__ == '__main__':
    config = Config()
    print(config.get_email("username"))
    print(config.get_db("port"))