#!/usr/bin/python
from core.action_page import ActionPage
from element.mail163_element import Mail163Element


class Mail163Page(ActionPage):

    # 基础业务封装
    def open_page(self):
        self.open_url("https://mail.163.com/")

    def switch_to_frame(self):
        self.switch_frame(Mail163Element.frame_loc)

    def input_username(self, username):
        self.send_value(Mail163Element.username_loc, username)

    def input_password(self, password):
        self.send_value(Mail163Element.password_loc, password)

    def login_action(self):
        self.click(Mail163Element.login_btn_loc)

    def get_assert_text(self):
        return self.get_text(Mail163Element.assert_text_loc)

    # 业务逻辑封装
    def login_163mail_business(self, username, password):
        self.open_page()
        self.switch_to_frame()
        self.input_username(username)
        self.input_password(password)
        self.login_action()


if __name__ == '__main__':
    pass