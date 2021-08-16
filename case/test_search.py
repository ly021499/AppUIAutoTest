#!/usr/bin/python
from pages.search_page import SearchPage
from selenium import webdriver
from tool.tools import get_yaml_path
import ddt
import unittest


@ddt.ddt
class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        driver = webdriver.Chrome()
        cls.search_page = SearchPage(driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.search_page.close()

    @ddt.file_data(get_yaml_path("search.yaml"))
    @ddt.unpack
    def search_fei(self, **kwargs):
        keyword = kwargs["keyword"]
        self.search_page.open_page()
        self.search_page.input_value(keyword)
        self.search_page.click_button()


if __name__ == '__main__':
    unittest.main()
