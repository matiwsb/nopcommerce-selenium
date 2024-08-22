import string
from utilities.custom_logger import Log_Maker
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from utilities.custom_logger import Log_Maker
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Add_Customer_Page import Add_Customer_Page
from configurations.generators import generate_random_password, generate_random_email

class Test_03_Add_New_Customer:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "random@dupadupa.com"
    logger = Log_Maker.log_gen()


    def test_add_new_customer(self, setup):
        self.logger.info("TEST_03_ADD_NEW_CUSTOMER")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_password(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("LOGIN COMPLETED")
        self.logger.info("ADDING NEW CUSTOMER")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.add_customer.click_addnew()
        self.logger.info("PROVIDING CUSTOMER INFO STARTED")
        email = generate_random_email()
        self.add_customer.enter_email(email)
        password = generate_random_password()
        self.add_customer.enter_password(password)
        self.add_customer.enter_firstname('Dzon')
        self.add_customer.enter_lastname('Tom')
        self.add_customer.select_gender('Male')
        self.add_customer.enter_dob('12/12/2002')
        self.add_customer.enter_companyname('MyCompany')
        self.add_customer.select_tax_exempt()
        self.add_customer.select_newsletter("Your store name")
        self.logger.info("Your store selected")
        self.add_customer.select_customer_role('Registered')
        self.add_customer.select_manager_of_vendor('Vendor 1')
        self.add_customer.enter_admin_comments('Test admin comment')
        self.add_customer.click_save()
        time.sleep(3)
        customer_add_success_text = "The new customer has been added successfully."
        success_text = self.driver.find_element(By.XPATH, "//div[@class='content-wrapper']/div[1]").text

        if customer_add_success_text in success_text:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_new_customer.png")
            self.driver.close()
            assert False


# def generate_random_email():
#     username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
#     domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])
#     return f'{username}@{domain}'

# def generate_random_password():
#     password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
#     return f'{password}'

