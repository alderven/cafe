import time
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT = 1
WAIT_SEL = 10


def find_by_xpath(driver, xpath):
    wait = WebDriverWait(driver, WAIT_SEL)
    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    time.sleep(WAIT)
    return el


def accept_alert(driver):
    alert = driver.switch_to_alert()
    alert.accept()


class LoginPage:

    @staticmethod
    def enter_username(driver, config, value):
        el = find_by_xpath(driver, config['LOCATORS']['LoginField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def enter_password(driver, config, value):
        el = find_by_xpath(driver, config['LOCATORS']['PasswordField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def click_login_button(driver, config):
        find_by_xpath(driver, config['LOCATORS']['LoginButton']).click()

    @staticmethod
    def click_logout_button(driver, config):
        find_by_xpath(driver, config['LOCATORS']['LogoutButton']).click()

    @staticmethod
    def click_delete_button(driver, config):
        find_by_xpath(driver, config['LOCATORS']['DeleteButton']).click()

    @staticmethod
    def get_error_message(driver, config):
        el = find_by_xpath(driver, config['LOCATORS']['LoginErrorMessage'])
        return el.text

    @staticmethod
    def get_credentials(driver, config):
        el = find_by_xpath(driver, config['LOCATORS']['Credentials'])
        el = el.text.split('"')
        username = el[1]
        password = el[3]
        return username, password


class EmployeesPage:

    @staticmethod
    def get_greeting_text(driver, config):
        el = find_by_xpath(driver, config['LOCATORS']['Greeting'])
        return el.text

    @staticmethod
    def click_create_button(driver, config):
        find_by_xpath(driver, config['LOCATORS']['CreateButton']).click()

    @staticmethod
    def click_edit_button(driver, config):
        find_by_xpath(driver, config['LOCATORS']['EditButton']).click()

    @staticmethod
    def click_delete_button(driver, config):
        find_by_xpath(driver, config['LOCATORS']['DeleteButton']).click()

    @staticmethod
    def select_element_in_the_list(driver, config, index):
        find_by_xpath(driver, config['LOCATORS']['CreateButton'].replace('{i}', str(index))).click()

    class Create:

        @staticmethod
        def click_add_button(driver, config):
            find_by_xpath(driver, config['LOCATORS']['AddButton']).click()

        @staticmethod
        def click_cancel_button(driver, config):
            find_by_xpath(driver, config['LOCATORS']['CancelButton']).click()

        @staticmethod
        def fill_first_name_field(driver, config, value):
            el = find_by_xpath(driver, config['LOCATORS']['FirstNameField'])
            el.clear()
            el.send_keys(value)

        @staticmethod
        def fill_last_name_field(driver, config, value):
            el = find_by_xpath(driver, config['LOCATORS']['LastNameField'])
            el.clear()
            el.send_keys(value)

        @staticmethod
        def fill_start_date_field(driver, config, value):
            el = find_by_xpath(driver, config['LOCATORS']['StartDateField'])
            el.clear()
            el.send_keys(value)

        @staticmethod
        def fill_email_field(driver, config, value):
            el = find_by_xpath(driver, config['LOCATORS']['EmailField'])
            el.clear()
            el.send_keys(value)

        @staticmethod
        def get_all_employees(driver, config):
            return find_by_xpath(driver, config['LOCATORS']['EmployeesList']).text

    class Edit:

        @staticmethod
        def click_update_button(driver, config):
            find_by_xpath(driver, config['LOCATORS']['UpdateButton']).click()


def generate_random_string():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))
