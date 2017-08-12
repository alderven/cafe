# PURPOSE OF THE PROJECT

This projects is dedicated to the testing of following web site:
http://cafetownsend-angular-rails.herokuapp.com/

The Allure web page with the results of a sample test run can be found here: https://cdn.rawgit.com/alderven/cafe/master/allure-report/index.html

### DISCLAIMER ###
* *There are only "smoke" tests written in the project. There are far more tests can be written to cover full functionality*
* *Project compatible with the Windows platform only (but can be extended to support other platforms since Python and other tools are crossplatfrom)*
* *Tests are run in Chrome browser only (but again project can be easily improved to include other browsers)*

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
1. At the end you will get test run results. It will contain some brief information about test results
```javascript
==================== 1 failed, 5 passed in 92.04 seconds =====================
```
But to get more representative results we are going to generate Allure report.

# HOW TO GENERATE ALLURE REPORT:
We are using Allure Framework to get nice and detailed representation of the results.

You need to execute following line in a Command Prompt:
```javascript
allure serve full_path_to_report_folder
```
Generated Allure report will be shown in your browser.

Here is the one that was generated for this project: https://cdn.rawgit.com/alderven/cafe/master/allure-report/index.html

You can find a lot of helpful information in the Allure report such as:

* Overall test run status:
![Status](https://raw.githubusercontent.com/alderven/cafe/master/imgs/Status.png)
* Features which were tested (here you can see that all blocking functionality is fine and one critical functionality was broken):
![Severity](https://raw.githubusercontent.com/alderven/cafe/master/imgs/Severity.png)
* Features which were tested:
![Severity](https://raw.githubusercontent.com/alderven/cafe/master/imgs/Features.png)
* Details of each test case with every step described on a business level:
![Test Case details](https://github.com/alderven/cafe/blob/master/imgs/TestSteps.png)
* ... And tons of other helpful information: : https://cdn.rawgit.com/alderven/cafe/master/allure-report/index.html

# TECHNICAL BACKGROUND
Following technologies were used:
* Python: scripting language for writing tests
* Pytest: test framework for Python for better tests organization
* Selenium WebDriver: allows to interact with the web browser
* Allure Framework: allows to generate web page with the nice representation of test results
