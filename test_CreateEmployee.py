import names
import pytest
import datetime
import methods


@pytest.allure.feature('Create employee')
@pytest.allure.story('Create new employee')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_create_new_employee(driver, config, login):

    with pytest.allure.step('Click "Create" button'):
        methods.EmployeesPage.click_create_button(driver, config)

    with pytest.allure.step('Fill "First name" field'):
        first_name = names.get_first_name()
        methods.EmployeesPage.Create.fill_first_name_field(driver, config, first_name)

    with pytest.allure.step('Fill "Last name" field'):
        last_name = names.get_last_name()
        methods.EmployeesPage.Create.fill_last_name_field(driver, config, last_name)

    with pytest.allure.step('Fill "Start date" field'):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        methods.EmployeesPage.Create.fill_start_date_field(driver, config, date)

    with pytest.allure.step('Fill "Email" field'):
        email = '{}.{}@gmail.com'.format(first_name, last_name)
        methods.EmployeesPage.Create.fill_email_field(driver, config, email)

    with pytest.allure.step('Click "Add" button'):
        methods.EmployeesPage.Create.click_add_button(driver, config)

    with pytest.allure.step('Check, than new employee is in the employees list'):
        employees_list = methods.EmployeesPage.Create.get_all_employees(driver, config)
        employee_full_name = '{} {}'.format(first_name, last_name)
        err_msg = '"{}" not found in the employees list:\n{}'.format(employee_full_name, employees_list)
        assert employee_full_name in employees_list, err_msg


@pytest.allure.feature('Create employee')
@pytest.allure.story('Adding same employee twice should be restricted')
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_add_same_employee_twice(driver, config, new_employee):

    with pytest.allure.step('Add same employee again'):

        with pytest.allure.step('Click "Create" button'):
            methods.EmployeesPage.click_create_button(driver, config)

        with pytest.allure.step('Fill "First name" field'):
            methods.EmployeesPage.Create.fill_first_name_field(driver, config, new_employee['firstName'])

        with pytest.allure.step('Fill "Last name" field'):
            methods.EmployeesPage.Create.fill_last_name_field(driver, config, new_employee['lastName'])

        with pytest.allure.step('Fill "Start date" field'):
            methods.EmployeesPage.Create.fill_start_date_field(driver, config, new_employee['date'])

        with pytest.allure.step('Fill "Email" field'):
            methods.EmployeesPage.Create.fill_email_field(driver, config, new_employee['email'])

        with pytest.allure.step('Click "Add" button'):
            methods.EmployeesPage.Create.click_add_button(driver, config)

    with pytest.allure.step('Check, that there is only one created employee in the employees list'):
        employees = methods.EmployeesPage.Create.get_all_employees(driver, config)
        employees_count = employees.count('{} {}'.format(new_employee['firstName'], new_employee['lastName']))
        err_msg = 'Expected 1 employee. Got: {}'.format(employees_count)
        assert employees_count == 1, err_msg
