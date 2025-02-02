from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from pages.main_page import MainPage
from selenium.webdriver.firefox.options import Options


from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    driver_path = GeckoDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Firefox(service=service)

    firefox_options = Options()
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)



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


# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
#
#
#
# firefox_options = Options()
# firefox_options.add_argument('--headless')
# driver = webdriver.Firefox(options=firefox_options)
#
#
# driver.get("https://soft.reelly.io/sign-up")
#
# driver.quit()
