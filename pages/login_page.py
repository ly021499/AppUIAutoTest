#!/usr/bin/python
from core.action_page import ActionPage
from element.login_element import LoginElement


class LoginPage(ActionPage):

    # 基础业务封装
    def access_permission(self):
        element = self.locate_element(LoginElement.allow_button)
        if self.is_displayed(element):
            self.click(LoginElement.allow_button)
        else:
            pass

    def click_account_login(self):
        self.click(LoginElement.account_login_element)

    def get_assert_text(self):
        return self.get_text(LoginElement.assert_text_element)

    # 业务逻辑封装
    def account_login_action(self, account, password):
        self.click_account_login()
        self.send_value(LoginElement.account_element, account)
        self.send_value(LoginElement.password_element, password)
        self.click(LoginElement.login_element)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.open_page()
    lp.account_login_action("t0301528378", "Mozart1998.?")
    import time
    time.sleep(1)
    text = driver.find_element_by_xpath('//div[@class="userinfo-top"]/p').text
    print(text)

