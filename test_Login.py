import names
import pytest
import methods


@pytest.allure.feature('Login')
@pytest.allure.story('Login with invalid credentials')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_login_invalid_credentials(driver, config):

    with pytest.allure.step('Enter invalid Username'):
        invalid_username = names.get_first_name()
        methods.LoginPage.enter_username(driver, config, invalid_username)

    with pytest.allure.step('Enter invalid Password'):
        invalid_password = names.get_last_name()
        methods.LoginPage.enter_password(driver, config, invalid_password)

    with pytest.allure.step('Click "Login" button'):
        methods.LoginPage.click_login_button(driver, config)

    with pytest.allure.step('Check, that error message displays'):
        error = methods.LoginPage.get_error_message(driver, config)
        assert error == 'Invalid username or password!'


@pytest.allure.feature('Login')
@pytest.allure.story('Login and Logout')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_login_logout(driver, config):

    with pytest.allure.step('Get Username and Password from the Login page'):
        username, password = methods.LoginPage.get_credentials(driver, config)

    with pytest.allure.step('Enter valid Username'):
        methods.LoginPage.enter_username(driver, config, username)

    with pytest.allure.step('Enter valid Password'):
        methods.LoginPage.enter_password(driver, config, password)

    with pytest.allure.step('Click "Login" button'):
        methods.LoginPage.click_login_button(driver, config)

    with pytest.allure.step('Check, that greeting appears'):
        greeting = methods.EmployeesPage.get_greeting_text(driver, config)
        assert greeting == 'Hello {}'.format(username)

    with pytest.allure.step('Press Logout button'):
        methods.LoginPage.click_logout_button(driver, config)

    with pytest.allure.step('Check, that Login page opens (Username and credentials are on the page'):
        methods.LoginPage.get_credentials(driver, config)
