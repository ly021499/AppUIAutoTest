#!/usr/bin/python
from core.action_page import ActionPage
from element.login_element import LoginElement


class LoginPage(ActionPage):

    # 基础业务封装
    def access_permission(self):
        for i in range(4):
            try:
                element = self.locate_element(LoginElement.allow_button_element)
                if self.is_displayed(element):
                    element.click()
            except:
                pass

    def agree_deal(self):
        self.locate_element(LoginElement.agree_deal_element).click()
        # self.click(LoginElement.agree_deal_element)

    def back_home_page(self):
        self.click(LoginElement.back_element)

    def account_login(self):
        self.click(LoginElement.account_login_element)

    def phone_login(self):
        self.click(LoginElement.phone_login_element)

    # 业务逻辑封装
    def account_login_action(self, account, password):
        self.account_login()
        self.send_value(LoginElement.account_element, account)
        self.send_value(LoginElement.password_element, password)
        self.click(LoginElement.login_element)


if __name__ == '__main__':
    from tool.tools import get_appium_driver
    driver = get_appium_driver()
    lp = LoginPage(driver)
    lp.access_permission()
    import time
    time.sleep(3)
    lp.agree_deal()
    lp.account_login_action('t0373805249', '123456')

