# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from app.application import Application
# from pages.main_page import MainPage
# # from selenium.webdriver.firefox.options import Options
#
#
# # from selenium.webdriver.firefox.service import Service
# # from webdriver_manager.firefox import GeckoDriverManager
#
#
# def browser_init(context):
#     """
#     :param context: Behave context
#     """
#     driver_path = ChromeDriverManager().install()
#     service = Service(driver_path)
#     context.driver = webdriver.Chrome(service=service)
#
#     # driver_path = GeckoDriverManager().install()
#     # service = Service(driver_path)
#     # context.driver = webdriver.Firefox(service=service)
#     #
#     # firefox_options = Options()
#     # firefox_options.add_argument('--headless')
#     # driver = webdriver.Firefox(options=firefox_options)
#
#
#
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(4)
#     context.driver.wait = WebDriverWait(context.driver, 15)
#     context.app = Application(context.driver)
#     context.main = MainPage(context.driver)
#
#
# def before_scenario(context, scenario):
#     print('\nStarted scenario: ', scenario.name)
#     browser_init(context)
#
#
# def before_step(context, step):
#     print('\nStarted step: ', step)
#
#
# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)
#
#
# def after_scenario(context, feature):
#     context.driver.quit()
#
#
# # from selenium import webdriver
# # from selenium.webdriver.firefox.options import Options
# #
# #
# #
# # firefox_options = Options()
# # firefox_options.add_argument('--headless')
# # driver = webdriver.Firefox(options=firefox_options)
# #
# #
# # driver.get("https://soft.reelly.io/sign-up")
# #
# # driver.quit()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from pages.main_page import MainPage
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def browser_init(context):
    """
    :param context: Behave context
    """

    username = "Sudhakaran Velluri"
    access_key = "Deadshotcrazy1@"


    desired_cap = {
        'browser': 'chrome',
        'browser_version': 'latest',
        'os': 'Windows',
        'os_version': '10',
        'name': 'My Test',
        'build': '1.0'
    }

    # If you want to run on Firefox:
    # desired_cap = {
    #     'browser': 'firefox',
    #     'browser_version': 'latest',
    #     'os': 'Windows',
    #     'os_version': '10',
    #     'name': 'My Test',
    #     'build': '1.0'
    # }

    # Initialize the WebDriver for BrowserStack
    context.driver = webdriver.Remote(
        command_executor=f'https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub', desired_capabilities=desired_cap )

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)
    context.main = MainPage(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.quit()

