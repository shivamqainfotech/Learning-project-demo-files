import random

from HtmlTestRunner import HTMLTestRunner
import unittest
from page_objects.demo_Register_page import demo_Register_page
from utils.Option_Parser import Option_Parser


class demo_Register_tests(unittest.TestCase):
    # Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
    base_url = options.url
    browser = options.browser
    browser_version = options.browser_version
    os_version = options.os_version
    os_name = options.os_name
    remote_flag = options.remote_flag
    testrail_flag = options.testrail_flag
    test_run_id = options.test_run_id
    demo_register = demo_Register_page()

    def __init__(self, testname, testcase=None):
        super(demo_Register_tests, self).__init__(testname)
        self._testcase = testcase


    def setUp(self):
        self.demo_register.register_driver(self.remote_flag, self.os_name, self.os_version, self.browser,
                                           self.browser_version)

    def test_01_sign_up_page(self):
        value=int(random.uniform(0,100000))
        institution_name="Reef Education"
        reef_id01="automation_testing@reef-education.com"
        UserPassword="123Qwerty"
        for num in range(100):
            email_id01=first_name01.lower()+"_"+last_name01+str(value)+'@reef-education.com'
        self.demo_register.sign_up_page_click_signup()
        self.demo_register.search_institution_name_box(institution_name)
        self.demo_register.select_institution_name()
        self.demo_register.click_on_next_button()
        self.demo_register.enter_first_name(first_name=first_name01)
        self.demo_register.enter_last_name(last_name=last_name01)
        self.demo_register.enter_email_id(email_id=email_id01)
        self.demo_register.enter_reef_id(reef_id=reef_id01)
        self.demo_register.click_on_checkbox_of_terms()
        self.demo_register.click_on_next_button_after_details_filled()
        self.demo_register.select_password(UserPassword)
        self.demo_register.select_confirm_password(UserPassword)
        self.demo_register.create_account()

    # def test_01_registration(self):
    #     title = self.demo_register.get_window_title_for_us()
    #     self.assertEqual(title, "Reef Create Account - Find Your Institution", "Does'nt match")

    # def tearDown(self):
    #     self.create_account_page.driver.delete_all_cookies()
    #     self.create_account_page.teardown(obj=self)

    def test_enter_credentials_for_login(self):
        self.demo_register.enter_email_id_for_login(email_id01)
        self.demo_register.enter_password_for_login(UserPassword)
        self.demo_register.click_on_sign_in()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(demo_Register_tests)
    first_name01="Automation"
    last_name01="Testing"
    email_id01="automation_testing@gmail.com"
    UserPassword="123Qwerty"
    runner = HTMLTestRunner(output='Regression')
    runner.run(suite)
