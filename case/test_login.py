#!/usr/bin/python
from pages.login_page import LoginPage
from selenium import webdriver
from tool.tools import get_yaml_path
import ddt
import unittest


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.login_page.close()

    @ddt.file_data(get_yaml_path('login.yaml'))
    def test_login(self, **kwargs):
        account = kwargs['account']
        password = kwargs['password']
        assert_type = kwargs['assert_type']
        self.login_page.open_page()
        self.login_page.click_login_text()
        self.login_page.account_login_action(account, password)
        try:
            if assert_type == 1:
                self.assertEqual("No0b", self.login_page.get_assert_text())
            else:
                self.assertIn("注册", self.driver.page_source)
        except Exception as e:
            self.login_page.save_image()
            raise e


if __name__ == '__main__':
    unittest.main()
