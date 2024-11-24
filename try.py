from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:

    driver.get("https://www.target.com/")
    sleep(2)


    driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(2)

    # Step 3: Click SignIn from side navigation
    driver.find_element(By.XPATH, "//button[@type='button' and @data-test='accountNav-signIn']").click()
    sleep(2)

    # Step 4: Verify SignIn page opened
    # Verify "Sign into your Target account" text is shown
    expected_result= 'Found Sign into your Target account and Signin with password'
    actual = driver.find_element(By.XPATH, "//h1/span[contains(text(), 'Sign into your Target account')]").text
    actual_1 =driver.find_element(By.XPATH, "//button/span[contains(text(),'Sign in with password')]").text
    print(f"{actual} and {actual_1}")
    sleep(2)

finally:

    driver.quit()



options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

try:

    driver.get("https://www.target.com/")
    time.sleep(2)

    search_box = driver.find_element(By.ID, "search")
    search_box.send_keys("laptop")
    search_box.submit()
    time.sleep(2)

    results = driver.find_element(By.XPATH, "//span[contains(text(),'results')]")
    print(f"Search results found: {results.text}")

except Exception as e:
    print("Test Failed:", e)

finally:

    driver.quit()