import pytest
import datetime
import methods


@pytest.allure.feature('Edit employee')
@pytest.allure.story('Edit employee')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_delete_employee(driver, config, new_employee):

    with pytest.allure.step('Select created employee in the list'):
        employees = methods.EmployeesPage.Create.get_all_employees(driver, config)
        employees_list = employees.split('\n')
        employee_full_name = '{} {}'.format(new_employee['firstName'], new_employee['lastName'])
        index = employees_list.index(employee_full_name)
        methods.EmployeesPage.select_element_in_the_list(driver, config, index)

    with pytest.allure.step('Click "Edit" button'):
        methods.EmployeesPage.click_edit_button(driver, config)

    with pytest.allure.step('Update all fields'):

        with pytest.allure.step('Update "First name" field'):
            first_name = methods.generate_random_string()
            methods.EmployeesPage.Create.fill_first_name_field(driver, config, first_name)

        with pytest.allure.step('Update "Last name" field'):
            last_name = methods.generate_random_string()
            methods.EmployeesPage.Create.fill_last_name_field(driver, config, last_name)

        with pytest.allure.step('Update "Start date" field'):
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            methods.EmployeesPage.Create.fill_start_date_field(driver, config, date)

        with pytest.allure.step('Update "Email" field'):
            email = methods.generate_random_string() + '@gmail.com'
            methods.EmployeesPage.Create.fill_email_field(driver, config, email)

    with pytest.allure.step('Click "Update" button'):
        methods.EmployeesPage.Edit.click_update_button(driver, config)

    with pytest.allure.step('Check, that updated employee is in the list'):
        employees_list = methods.EmployeesPage.Create.get_all_employees(driver, config)
        employee_full_name = '{} {}'.format(first_name, last_name)
        err_msg = '"{}" not found in the employees list:\n{}'.format(employee_full_name, employees_list)
        assert employee_full_name in employees_list, err_msg
