#!/usr/bin/python
from core.action_page import ActionPage
from element.search_element import SearchElement


class SearchPage(ActionPage):

    # 基础业务逻辑封装
    def open_page(self):
        self.open_url("https://www.baidu.com")

    def input_value(self, keyword):
        self.send_value(SearchElement.input_loc, keyword)

    def click_button(self):
        self.click(SearchElement.click_loc)

    # 业务逻辑封装
    def search_word(self, keyword):
        self.open_page()
        self.input_value(keyword)
        self.click_button()


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    s = SearchPage(driver)
    s.open_page()
    s.input_value("刘亦菲")
    s.click_button()
    s.close()
    driver.find_element_by_xpath()

