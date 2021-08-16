#!/usr/bin/python
import unittest
import ddt
from core.config_log import logger
from tool.tools import get_yaml_path
from selenium import webdriver
from pages.mail163_page import Mail163Page


@ddt.ddt
class TestMail163Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        driver = webdriver.Chrome()
        cls.mail_page = Mail163Page(driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mail_page.close()

    @ddt.file_data(get_yaml_path("login163mail.yaml"))
    def test_mail163_login(self, **kwargs):
        username = kwargs["username"]
        password = kwargs["password"]
        assert_text = kwargs["assert_text"]
        self.mail_page.login_163mail_business(username, password)
        try:
            self.assertEqual(assert_text, self.mail_page.get_assert_text())
            logger.info("断言成功")
        except Exception as e:
            self.mail_page.save_image()
            logger.info("断言失败")
            raise e


if __name__ == '__main__':
    unittest.main()
