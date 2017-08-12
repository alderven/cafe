import os
import names
import pytest
import datetime
import methods
import configparser
from selenium import webdriver


@pytest.fixture(scope='module')
def config():

    cfg = configparser.ConfigParser()
    cfg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.cfg')
    cfg.read(cfg_path)
    return cfg


@pytest.yield_fixture(scope='function')
def driver(config):

    # Launch Driver
    driver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe')
    dr = webdriver.Chrome(driver_path)
    dr.get(config['SITE']['URL'])

    # Pass Driver instance to test
    yield dr

    # Quit Driver
    dr.quit()


@pytest.yield_fixture(scope='function')
def login(driver, config):

    username, password = methods.LoginPage.get_credentials(driver, config)
    methods.LoginPage.enter_username(driver, config, username)
    methods.LoginPage.enter_password(driver, config, password)
    methods.LoginPage.click_login_button(driver, config)
    greeting = methods.EmployeesPage.get_greeting_text(driver, config)
    assert greeting == 'Hello {}'.format(username)


@pytest.yield_fixture(scope='function')
def new_employee(driver, config, login):

    methods.EmployeesPage.click_create_button(driver, config)

    first_name = names.get_first_name()
    methods.EmployeesPage.Create.fill_first_name_field(driver, config, first_name)

    last_name = names.get_last_name()
    methods.EmployeesPage.Create.fill_last_name_field(driver, config, last_name)

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    methods.EmployeesPage.Create.fill_start_date_field(driver, config, date)

    email = '{}.{}@gmail.com'.format(first_name, last_name)
    methods.EmployeesPage.Create.fill_email_field(driver, config, email)

    methods.EmployeesPage.Create.click_add_button(driver, config)

    employee_list = methods.EmployeesPage.Create.get_all_employees(driver, config)
    assert '{} {}'.format(first_name, last_name) in employee_list

    return {'firstName': first_name, 'lastName': last_name, 'date': date, 'email': email}
