from pages.internship_page import InternshipPage
from pages.base_page import BasePage
from pages.cart_message import Cart
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page= BasePage(driver)
        self.header =   Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart = Cart(driver)
        self.internship_page = InternshipPage(driver)
        self.login_page = LoginPage(driver)
        self.settings_page = SettingsPage(driver)



