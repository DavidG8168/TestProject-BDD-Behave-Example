from behave import *


@given('I navigate to the TestProject example page')
def step_impl(context):
    context.driver.get("https://example.testproject.io/web/")


@when('I perform a login')
def step_impl(context):
    context.driver.find_element_by_css_selector("#name").send_keys("John Smith")
    context.driver.find_element_by_css_selector("#password").send_keys("12345")
    context.driver.find_element_by_css_selector("#login").click()


@then('I should see a logout button')
def step_impl(context):
    passed = context.driver.find_element_by_css_selector("#logout do not exists").is_displayed()
    assert passed is True
