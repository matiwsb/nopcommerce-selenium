import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_Admin_Page import Login_Admin_Page


class Test_01_Admin_Login:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "random@dupadupa.com"
    logger = Log_Maker.log_gen()

    def test_title_verification(self, setup):
        self.logger.info("@@@@@@@@@TC1@@@@@@@@")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        expected_title = "Your store. Login"
        if actual_title == expected_title:
            assert True
            self.logger.info("@@@@@@@@@PASS@@@@@@@@")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.info("@@@@@@@@@FALSE@@@@@@@@")
            assert False

    def test_valid_admin_login(self, setup):
        self.logger.info("@@@@@@@@@TC2@@@@@@@@")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        actual_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        expected_dashboard_text = "Dashboard"
        if actual_dashboard_text == expected_dashboard_text:
            assert True
            self.logger.info("@@@@@@@@@PASS@@@@@@@@")
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.quit()
            self.logger.info("@@@@@@@@@FALSE@@@@@@@@")
            assert False

    def test_invalid_admin_login(self, setup):
        self.logger.info("@@@@@@@@@TC3@@@@@@@@")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH, "//li").text
        if error_message == "No customer account found":
            assert True
            self.logger.info("@@@@@@@@@PASS@@@@@@@@")
            self.driver.quit()
        else:
            self.driver.quit()
            self.logger.info("@@@@@@@@@FALSE@@@@@@@@")
            assert False