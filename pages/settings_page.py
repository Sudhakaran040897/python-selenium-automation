from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingsPage(BasePage):

    SETTINGS_MENU = (By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")

    VERIFICATION_OPTION = (By.CSS_SELECTOR, "[href='/verification/step-0']")

    UPLOAD_IMAGE_BUTTON = (By.CSS_SELECTOR, "[class='upload-button-2']")


    NEXT_STEP_BUTTON = (By.CSS_SELECTOR, "[wized='nextButtonStep0']")

    def open_settings(self):
        # self.driver.find_element(*self.SETTINGS_MENU).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SETTINGS_MENU)).click()

    def open_verification(self):
        self.driver.find_element(*self.VERIFICATION_OPTION).click()

    def is_verification_page_open(self):
        return self.driver.current_url == "https://soft.reelly.io/verification/step-0"

    def are_buttons_present(self):
        upload_image_present = self.UPLOAD_IMAGE_BUTTON
        next_step_present = self.NEXT_STEP_BUTTON
        return upload_image_present and next_step_present