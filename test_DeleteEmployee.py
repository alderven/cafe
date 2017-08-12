import pytest
import methods


@pytest.allure.feature('Delete employee')
@pytest.allure.story('Delete employee')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_delete_employee(driver, config, new_employee):

    with pytest.allure.step('Find created employee in the list'):
        methods.EmployeesPage.find_employee_by_full_name(driver, config, new_employee['firstName'], new_employee['lastName'])

    with pytest.allure.step('Click "Delete" button'):
        methods.EmployeesPage.click_delete_button(driver, config)

    with pytest.allure.step('Confirm deleting'):
        methods.accept_alert(driver)

    with pytest.allure.step('Check, that created employee is not in the list anymore'):
        employees_list = methods.EmployeesPage.Create.get_all_employees(driver, config)
        employee_full_name = '{} {}'.format(new_employee['firstName'], new_employee['lastName'])
        err_msg = '"{}" found in the employees list:\n{}'.format(employee_full_name, employees_list)
        assert employee_full_name not in employees_list, err_msg
