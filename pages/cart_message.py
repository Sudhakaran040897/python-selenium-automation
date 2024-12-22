from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Cart(BasePage):
    CART_INFO = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def message(self):
        empty_cart_message = self.driver.find_element(*self.CART_INFO)
        print("Message found: ", empty_cart_message.text)
        assert "Your cart is empty" in empty_cart_message.text