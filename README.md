# PURPOSE OF THE PROJECT

This projects is dedicated to the testing of following web site:
http://cafetownsend-angular-rails.herokuapp.com/

The Allure web page with the results of a sample test run can be found here:

### DISCLAIMER ###
* *There are only "smoke" tests written in the project. There are far more tests can be written to cover full functionality*
* *Project compatible with the Windows platform only (but can be extended to the other platforms since Python and other tools are crossplatfrom)*
* *Tests are run in Chrome browser only (but again project can be easily improved to involve other browsers)*

# HOW TO INSTALL:
1. Download and unzip this project: https://github.com/alderven/cafe/archive/master.zip
1. Install Python 3.6 or higher: https://www.python.org/downloads/
1. Install following Python libs:
   * pytest: https://docs.pytest.org/en/latest/getting-started.html
   * selenium: https://pypi.python.org/pypi/selenium
   * pytest-allure-adaptor https://pypi.python.org/pypi/pytest-allure-adaptor
1. Download and unzip Chrome driver to the project root folder:
   https://sites.google.com/a/chromium.org/chromedriver/downloads
1. Install Allure Framework. See detailed instruction: https://docs.qameta.io/allure/latest/

# HOW TO RUN TESTS:
1. Launch Command Prompt (cmd.exe) in the project folder
1. Execute following line in Command Prompt:
```javascript
python -m pytest --alluredir report
```
1. At the end you will get testrun results. It will be something like that
```javascript
==================== 1 failed, 5 passed in 92.04 seconds =====================
```

# HOW TO GENERATE ALLURE REPORT:
We are using Allure Framework to get nice and detailed representation of the results.
Execute following line in Command Prompt:
```javascript
allure serve full_path_to_report_folder
```
The page is opening in your browser.
You can found a lot of helpful information about run:
In general you can see that 5 tests are passed and 1 with NORMAL criticity is failed.

# TECHNICAL BACKGROUND
Following technologies were used:
* Python: scripting language for writing tests
* Pytest: test framework for Python for better tests organization
* Selenium WebDriver: allows to interact with the web browser
* Allure Framework: allows to generate web site with the test results
