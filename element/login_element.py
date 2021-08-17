#!/usr/bin/python


class LoginElement:

    # 账号权限获取
    allow_button_element = ("xpath", '//*[@text="允许"]')
    # 同意协议
    agree_deal_element = ('id', 'com.sgkt.phone:id/tv_agree')
    # 返回
    back_element = ("id", 'com.sgkt.phone:id/iv_back')
    # 登录方式-账号登录
    account_login_element = ("xpath", '//*[@text="账号登录"]')
    # 登录方式-账号登录
    phone_login_element = ("id", 'com.sgkt.phone:id/btn_login_phone')

    # 账号输入框
    account_element = ("xpath", '//*[@text="请输入手机号或潭州账号"]')
    # 密码输入框
    password_element = ("xpath", '//*[@text="请输入密码"]')
    # 登录按钮
    login_element = ('id', 'com.sgkt.phone:id/btn_login')

