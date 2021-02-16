from src.testproject.sdk.drivers import webdriver
from src.testproject.decorator.behave_reporter import behave_reporter

""" Executed once per test run: Before any features and scenarios are run.
    Initialize the driver and start the session.
"""


@behave_reporter()
def before_all(context):
    context.driver = webdriver.Chrome(token="Hg3fwHF6lSXmEnWGfkRR6-ASK5jAuhbfDIA8rSfqPNM1",
                                      project_name="Behave Tests",
                                      job_name="Login Scenario")


""" Executed after each step in the scenario.
    Reports the test step.
"""


@behave_reporter(screenshot=True)
def after_step(context, step):
    pass


""" Executed after each scenario in the feature.
    Reports the scenario as a test.
"""


@behave_reporter
def after_scenario(context, scenario):
    pass


""" Executed once per test run: after all features and scenarios are run.
    Quit the driver and close the session.
"""


def after_all(context):
    context.driver.quit()
