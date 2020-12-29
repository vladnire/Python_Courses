from behave import given, when, then
from selenium import webdriver


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when('open orange hrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that the logo is present on page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.close()
