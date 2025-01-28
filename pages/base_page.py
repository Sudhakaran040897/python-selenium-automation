
class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def open_url(self, url):
        self.driver.get(url)


    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)


    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        class BasePage:
            def __init__(self, driver):
                self.driver = driver
                self.wait = WebDriverWait(driver, 10)

            def is_element_present(self, locator):
                try:
                    self.wait.until(EC.presence_of_element_located(locator))
                    return True
                except:
                    return False