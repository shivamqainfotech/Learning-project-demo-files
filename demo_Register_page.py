import time

from locator.demo_Register_locator import demo_Register_locator
from .Base_Page import Base_Page
from utils.Option_Parser import Option_Parser


class demo_Register_page(Base_Page, demo_Register_locator):
    """Page Object for the tutorial's main page"""
    op = Option_Parser().get_options()

    def launch_page(self):
        url = '#/account/login/'
        self.open(url)
        time.sleep(1)

    def sign_up_page_click_signup(self):
        self.sign_up_button_click

    def search_institution_name_box(self, name_of_institution):
        self.search_institution_box_.send_keys(name_of_institution)

    def select_institution_name(self):
        self.select_institution_name_given_list_click

    def click_on_next_button(self):
        self.next_button_after_institution_search_click

    def enter_first_name(self, first_name):
        self.set_text(self.first_name_box, first_name)

    def enter_last_name(self, last_name):
        self.last_name_box_.send_keys(last_name)

    def enter_email_id(self, email_id):
        self.email_id_box_.send_keys(email_id)

    def enter_reef_id(self, reef_id):
        self.reef_id_box_.send_keys(reef_id)

    def click_on_checkbox_of_terms(self):
        self.policy_checkbox_button_click

    def click_on_next_button_after_details_filled(self):
        self.next_button_after_details_click

    def select_password(self, userpassword):
        self.set_text(self.password, userpassword)

    def select_confirm_password(self, userpassword2):
        self.set_text(self.confirm_password, userpassword2)

    def create_account(self):
        self.click_element(self.create_account_click01)

    def enter_email_id_for_login(self,email_id_of_account_wants_to_login):
        self.set_text(self.login_email_id,email_id_of_account_wants_to_login)

    def enter_password_for_login(self,password_of_account_wants_to_login):
        self.set_text(self.user_password,password_of_account_wants_to_login)

    def click_on_sign_in(self):
        self.sign_in_button_for_login_click

    def get_window_title_for_us(self):
        return self.driver.title


