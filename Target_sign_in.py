from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
try:
    # Step 1: Open the Target website
    driver.get("https://www.target.com/")
    sleep(2)

    # Step 2: Click the SignIn button
    driver.find_element(By.XPATH, "//a[@class='sc-15d3e3b1-1 sc-58ad44c0-1 eOOysd libdhi']").click()
    sleep(2)

    # Step 3: Click SignIn from side navigation
    driver.find_element(By.XPATH, "//button[@class='sc-ddc722c0-0 sc-f1230b39-0 jKTcnK doBYzz h-margin-t-x2 h-margin-b-default']").click()
    sleep(2)

    # Step 4: Verify SignIn page opened
    # Verify "Sign into your Target account" text is shown
    driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']")
    print("SignIn Text Found")
    sleep(2)

finally:
    # Close the browser
    driver.quit()
