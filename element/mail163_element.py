#!/usr/bin/python


class Mail163Element:

    frame_loc = ("xpath", '//*[@id="loginDiv"]/iframe')
    username_loc = ("name", "email")
    password_loc = ("name", "password")
    login_btn_loc = ("id", "dologin")
    assert_text_loc = ("xpath", '//div[@class="ferrorhead"]')
