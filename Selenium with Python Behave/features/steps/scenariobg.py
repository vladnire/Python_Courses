from behave import given, when, then
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


@given('I launch browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('I open application')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter valid username "{user}" and password "{password}"')
def enter_credentials(context, user, password):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(password)


@when('Click on login')
def login(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('User must successfully login')
def verify_login(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except NoSuchElementException:
        assert False, "Login Failed"
    else:
        assert True, "Login Successful"
    finally:
        context.driver.close()


@when('Navigate to my info page')
def info_page(context):
    context.driver.find_element_by_id("menu_pim_viewMyDetails").click()


@then('My info page should display correct name')
def check_name(context):
    name = context.driver.find_element_by_xpath("//div[@id='profile-pic']//h1").text
    assert "Collings" in name


@when('Navigate to Buzz page')
def buzz_page(context):
    context.driver.find_element_by_id("menu_buzz_viewBuzz").click()


@then('Check Buzz page')
def check_buzz(context):
    status = context.driver.find_element_by_id('createPost_content').is_displayed()
    assert status is True
