# Selenium with Python Hybrid Framework

https://www.youtube.com/watch?v=57pjD89IFXA&list=PLUDwpEzHYYLt2RzOb-_eafLAP0VSoyJhf&ab_channel=SDET-QAAutomationTechie
Python, Selenium, Pytest, Page Object Model, HTML Reports

## Prerequisites

```
selenium
pytest
pytest-html
pytest-xdist
openpyxl
allure-pytest
chromedriver.exe (add chromediver to eg: Python\Python39\Scripts\ which need to be added to system path)
geckodriver.exe (add to eg: Python\Python39\Scripts\ which need to be added to system path)
msedgedriver.exe and rename it to MicrosoftWebDriver.exe (add to eg: Python\Python39\Scripts\ which need to be added to system path)
```

## Documentation

```
Framework Design.txt
Framework Steps.docx
```

## Usage

```
pytest -v -s test_cases\test_login.py
pytest -v -s test_cases\test_login.py –-browser chrome
pytest -v -s test_cases\test_login.py –-browser firefox
pytest -v -s -n=2 test_cases\test_login.py –-browser chrome #can't run test in parallel for now :(
pytest -v --html=reports\report.html --browser chrome # without -s to capture output in report, but will aldo capture stdout
pytest -s -v --html=reports\report.html test_cases\test_login_dtt.py --browser chrome
pytest -s -v -p no:warnings test_cases\test_add_customer.py --browser chrome # -p no:warnings to ignore custom marks warnings
pytest -s -v test_cases\test_search_customer_by_email.py --browser chrome
pytest -s -v test_cases\test_search_customer_by_name.py --browser chrome
pytest -s -v -m "sanity" --html=.\reports\report.html test_cases\ --browser chrome # you can use multiple marker values with and/or
```
