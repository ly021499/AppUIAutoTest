#!/usr/bin/python
from pages.login_page import LoginPage
from tool import tools
from tool.tools import get_yaml_path
import time
import ddt
import unittest


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = tools.get_appium_driver()
        self.login_page = LoginPage(self.driver)
        self.login_page.access_permission()
        self.login_page.agree_deal()

    def tearDown(self) -> None:
        time.sleep(3)
        self.login_page.close_app()

    @ddt.file_data(get_yaml_path('login.yaml'))
    def test_login(self, **kwargs):
        account = kwargs['account']
        password = kwargs['password']
        try:
            self.login_page.account_login_action(account, password)
        except Exception as e:
            self.login_page.save_image()
            raise e


if __name__ == '__main__':
    unittest.main()
