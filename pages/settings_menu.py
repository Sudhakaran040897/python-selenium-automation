from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SettingsMenu(BasePage):
    SETTINGS =(By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")

    def open_settings_page(self):
        settings_page = self.driver.find_element(*self.SETTINGS)

