# 程序的入口，执行文件
import multiprocessing
import os.path
import unittest
from tool.HTMLTestRunner import HTMLTestRunner
from core.read_config import config
from core.config_log import logger
import time


class Run(object):

    def __init__(self):
        self.tester = config.get_report("tester")
        self.title = config.get_report("title")
        self.description = config.get_report("description")

    def main(self):
        date = time.strftime("%Y-%m-%d-%H-%M")
        # 测试报告存放路径
        report_path = config.REPORT_DIR + "\\TestReport_{}.html".format(date)
        # 用例存放目录
        case_dir = os.path.join(config.BASE_DIR, "case")
        # 收集测试用例
        suite = unittest.TestSuite()
        loader = unittest.defaultTestLoader
        founder = loader.discover(start_dir=case_dir)
        # 将测试用例添加进测试套件
        suite.addTests(founder)
        # 写入测试结果数据
        with open(report_path, mode='wb') as file:
            runner = HTMLTestRunner(stream=file,
                                    tester=self.tester,
                                    title=self.title,
                                    description=self.description)
            logger.info("// ** *** ** *** ** *** ** ***   Beginning Of The Test   ** *** ** *** ** *** ** *** //")
            runner.run(suite)
            logger.info("// ** *** ** *** ** *** ** ***   End Of The Test   ** *** ** *** ** *** ** *** //")

    def run(self):
        """
        多进程运行case
        """
        threads = []
        for i in range(3):
            t = multiprocessing.Process(target=self.main, args=(i,))
            threads.append(t)
        for j in threads:
            j.start()


if __name__ == '__main__':
    run = Run()
    run.main()


