import names
import pytest
import datetime
import methods


@pytest.allure.feature('Edit employee')
@pytest.allure.story('Edit employee')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_delete_employee(driver, config, new_employee):

    with pytest.allure.step('Find created employee in the list'):
        methods.EmployeesPage.find_employee_by_full_name(driver, config, new_employee['firstName'], new_employee['lastName'])

    with pytest.allure.step('Click "Edit" button'):
        methods.EmployeesPage.click_edit_button(driver, config)

    with pytest.allure.step('Update all fields'):

        with pytest.allure.step('Update "First name" field'):
            first_name = names.get_first_name()
            methods.EmployeesPage.Create.fill_first_name_field(driver, config, first_name)

        with pytest.allure.step('Update "Last name" field'):
            last_name = names.get_last_name()
            methods.EmployeesPage.Create.fill_last_name_field(driver, config, last_name)

        with pytest.allure.step('Update "Start date" field'):
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            methods.EmployeesPage.Create.fill_start_date_field(driver, config, date)

        with pytest.allure.step('Update "Email" field'):
            email = '{}.{}@gmail.com'.format(first_name, last_name)
            methods.EmployeesPage.Create.fill_email_field(driver, config, email)

    with pytest.allure.step('Click "Update" button'):
        methods.EmployeesPage.Edit.click_update_button(driver, config)

    with pytest.allure.step('Check, that updated employee is in the list'):
        employees_list = methods.EmployeesPage.Create.get_all_employees(driver, config)
        employee_full_name = '{} {}'.format(first_name, last_name)
        err_msg = '"{}" not found in the employees list:\n{}'.format(employee_full_name, employees_list)
        assert employee_full_name in employees_list, err_msg
