#!/usr/bin/python
from core.read_config import config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from core.config_log import logger
import time
import os


class ActionPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(8)
        self.duration = 1000

    def quit(self):
        logger.info("Quit the Appium Driver.")
        self.driver.quit()

    def close_app(self):
        self.sleep(2)
        logger.info("Closing The Application.")
        self.driver.close_app()

    def sleep(self, seconds: float):
        logger.info("Sleep for {} seconds".format(seconds))
        time.sleep(seconds)

    def is_displayed(self, element):
        """
        判断元素是否存在
        :param element: 元素对象（WebElement对象）
        :return:
        """
        value = element.is_displayed()
        return value

    def locate_element(self, loc: tuple):
        """
        定位元素方法
        :param loc: 定位器
        :return:
        """
        locator = loc

        try:
            # 注意:以下入参本身是元组，不需要加*
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element
        except NoSuchElementException:
            logger.error("Page not found the element: {}".format(locator))
        except Exception as e:
            logger.error("Locate Failed，Error:{}".format(e))

        return self.driver.find_element(locator)

    def send_value(self, loc: tuple, value: str, clear=True):
        """
        输入值
        :param loc: 定位器
        :param value: 输入数据
        :param clear: 是否清除
        :return:
        """
        element = self.locate_element(loc)

        if clear:
            element.clear()
        try:
            self.sleep(0.5)
            element.send_keys(value)
            logger.info("Input Value: {}".format(value))
        except Exception as e:
            logger.error("Faild to input: {}，Error: {}".format(value, e))

    def click(self, loc: tuple):
        """
        点击元素
        :param loc: 定位器
        :return:
        """
        element = self.locate_element(loc)
        try:
            element.click()
            logger.info("The element \' {} \' was clicked.".format(element.get_attribute('value')))
        except Exception as e:
            display = self.is_displayed(element)
            if display is True:
                self.sleep(3)
                element.click()
                logger.info('The element was clicked')
            else:
                self.save_image()
                logger.error('Failed to click the element, Error: {}'.format(e))

    def save_image(self):
        """
        截图
        :return:
        """
        timestamp = time.strftime('%Y%m%d_%H.%M.%S')
        img_path = os.path.join(config.REPORT_DIR, "images", '%s.png' % str(timestamp))
        self.driver.save_screenshot(img_path)
        print('screenshot:', timestamp, '.png')

    def get_attribute(self, loc: tuple, attribute: str):
        """
        获取元素属性
        :param loc: 定位器
        :param attribute: 属性名称
        :return:
        """
        try:
            element = self.locate_element(loc)
            return element.get_attribute(attribute)
        except Exception as e:
            logger.info("Failed to get attribute with %s" % e)
            self.save_image()
            raise

    def get_text(self, loc: tuple):
        """
        获取元素对象文本
        :param loc: 定位器
        :return:
        """
        try:
            self.sleep(0.5)
            text = self.locate_element(loc).text
            logger.info("Get the text: {}".format(text))
            return text
        except Exception as e:
            logger.error("Faild to Get the text: {} Error: {}".format(loc, e))

    def assert_in_page_source(self, data: str):
        """
        断言数据是否存在page_source资源中
        :param data:
        :return:
        """
        if data not in self.driver.page_source:
            logger.error("Assert Failed: {} not in page_source".format(data))
            return 0
        logger.info("Assert Passed: {} in page_source".format(data))
        return 1

    @property
    def width(self):
        """
        获取屏幕宽度
        :return:
        """
        return self.driver.get_window_size()['width']

    @property
    def height(self):
        """
        获取屏幕高度
        :return:
        """
        return self.driver.get_window_size()['height']

    def swipe_to_left(self, base=0.1):
        """
        从右向左滑动
        :param base:
        :return:
        """
        return self.driver.swipe(self.width * (1 - base),
                                 self.height * 0.5,
                                 self.width * base,
                                 self.height * 0.5,
                                 self.duration
                                 )

    def swipe_to_right(self, base=0.1):
        """
        从左向右滑动
        :param base:
        :return:
        """
        return self.driver.swipe(self.width * base,
                                 self.height * 0.5,
                                 self.width * (1 - base),
                                 self.height * 0.5,
                                 self.duration
                                 )

    def swipe_to_top(self, base=0.9):
        """
        从下向上滑动
        :param base:
        :return:
        """
        return self.driver.swipe(self.width * 0.5,
                                 self.height * base,
                                 self.width * 0.5,
                                 self.height * (1 - base),
                                 self.duration
                                 )

    def swipe_to_bottom(self, base=0.9):
        """
        从上向下滑动
        :param base:
        :return:
        """
        return self.driver.swipe(self.width * 0.5,
                                 self.height * (1 - base),
                                 self.width * 0.5,
                                 self.height * base,
                                 self.duration
                                 )
    

if __name__ == '__main__':
    pass
