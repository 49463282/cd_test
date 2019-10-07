from selenium import webdriver
import unittest
import time
import sys


class Cd_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("http://webuat.icaodong.com")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def tearDown(self):
        driver = self.driver
        driver.quit()

    def test_login(self):
        driver = self.driver
        driver.add_cookie({"name": "Admin-Token",
                           "value": "41404620-c368-4a68-bcfd-e12844e9c115"})
        driver.refresh()
        gs = driver.find_element_by_class_name("store-detail").text
        zh = driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div[2]/div").text

        try:
            self.assertIn(gs, "全部分公司")
            self.assertIn(zh, "18549811213")

        except AssertionError:
            now_time = time.strftime("%Y-%m-%d %H_%M_%S")
            info = sys.exc_info()[1]
            driver.get_screenshot_as_file("../images/%s %s.png" % (info, now_time))

            raise


if __name__ == '__main__':
    unittest.main()