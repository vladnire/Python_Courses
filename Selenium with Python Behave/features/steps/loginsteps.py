from behave import given, when, then
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


@given('I launch Chrome')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('I open Orange HRM Homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{password}"')
def enter_credentials(context, user, password):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(password)


@when('Click on login button')
def login(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('User must successfully login to the Dashboard page')
def verify_login(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except NoSuchElementException:
        assert False, "Login Failed"
    else:
        assert True, "Login Successful"
    finally:
        context.driver.close()
