import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

WAIT = 1
WAIT_SEL = 10


def find_by_xpath(driver, xpath):
    time.sleep(WAIT)
    wait = WebDriverWait(driver, WAIT_SEL)
    el = wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
    return el


def accept_alert(driver):
    WebDriverWait(driver, WAIT_SEL).until(ec.alert_is_present())
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
    def find_employee_by_full_name(driver, config, first_name, last_name):
        employees = EmployeesPage.Create.get_all_employees(driver, config)
        employees_list = employees.split('\n')
        employee_full_name = '{} {}'.format(first_name, last_name)
        index = employees_list.index(employee_full_name) + 1
        find_by_xpath(driver, config['LOCATORS']['EmployeesRow'].replace('{i}', str(index))).click()

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
