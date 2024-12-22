from features.steps.HM4 import CART_ICON
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class Header(BasePage):
    SEARCH_FIELDS = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELDS)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def cart_icon(self):
        self.click(*self.CART_ICON)