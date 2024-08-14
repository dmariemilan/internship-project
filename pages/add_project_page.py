from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class AddProjectPage(Page):
    YOUR_NAME = (By.ID, 'Your-name')
    COMPANY_NAME = (By.ID, 'Your-company-name')
    ROLE_IN_COMPANY = (By.ID, 'Role')
    AGE_OF_COMPANY = (By.ID, 'Age-of-the-company')
    PROJECT_COUNTRY = (By.ID, 'Country')
    PROJECT_NAME = (By.ID, 'Name-project')
    PHONE = (By.ID, 'Phone')
    EMAIL = (By.ID, 'Email-add-project')
    SEND_APPLY_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    def verify_project_page_opened(self):
        self.verify_partial_url('add-a-project')

    def test_information(self):
        self.input_text('Test Tester', *self.YOUR_NAME)
        self.input_text('Test', *self.COMPANY_NAME)
        self.input_text('AQA Engineer', *self.ROLE_IN_COMPANY)
        self.input_text('15', *self.AGE_OF_COMPANY)
        self.input_text('Canada', *self.PROJECT_COUNTRY)
        self.input_text('Open House', *self.PROJECT_NAME)
        self.input_text('555 555-5555', *self.PHONE)
        self.input_text('test@tester.com', *self.EMAIL)

    def verify_right_information(self):
        actual_name = self.driver.find_element(*self.YOUR_NAME).get_attribute('value')
        expected_name = 'Test Tester'
        assert expected_name == actual_name, f'expected {expected_name}, got {actual_name}'
        print(f'actual name is "{actual_name}"')

        actual_company = self.driver.find_element(*self.COMPANY_NAME).get_attribute('value')
        expected_company = 'Test'
        assert expected_company == actual_company, f'expected {expected_company}, got {actual_company}'
        print(f'actual company is "{actual_company}"')

        actual_role = self.driver.find_element(*self.ROLE_IN_COMPANY).get_attribute('value')
        expected_role = 'AQA Engineer'
        assert expected_role == actual_role, f'expected {expected_role}, got {actual_role}'
        print(f'actual role is "{actual_role}"')

        actual_age = self.driver.find_element(*self.AGE_OF_COMPANY).get_attribute('value')
        expected_age = '15'
        assert expected_age == actual_age, f'expected {expected_age}, got {actual_age}'
        print(f'actual age is "{actual_age}"')

        actual_country = self.driver.find_element(*self.PROJECT_COUNTRY).get_attribute('value')
        expected_country = 'Canada'
        assert expected_country == actual_country, f'expected {expected_country}, got {actual_country}'
        print(f'actual country is "{actual_country}"')

        actual_project = self.driver.find_element(*self.PROJECT_NAME).get_attribute('value')
        expected_project = 'Open House'
        assert expected_project == actual_project, f'expected {expected_project}, got {actual_project}'
        print(f'actual project is "{actual_project}"')

        actual_phone = self.driver.find_element(*self.PHONE).get_attribute('value')
        expected_phone = '555 555-5555'
        assert expected_phone == actual_phone, f'expected {expected_phone}, got {actual_phone}'
        print(f'actual phone is "{actual_phone}"')

        actual_email = self.driver.find_element(*self.EMAIL).get_attribute('value')
        expected_email = 'test@tester.com'
        assert expected_email == actual_email, f'expected {expected_email}, got {actual_email}'
        print(f'actual email is "{actual_email}"')

    def click_application_btn(self):
        self.click(*self.SEND_APPLY_BUTTON)
        sleep(3)










