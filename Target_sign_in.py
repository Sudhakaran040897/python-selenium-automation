from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options
import time

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()





driver = webdriver.Chrome()


driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
sleep(2)




amazon_logo = driver.find_element(By.XPATH, "//a/i[@role='img']")
print("Amazon Logo aria-label:", amazon_logo.get_attribute("aria-label"))


email_field = driver.find_element(By.XPATH, "//input[@name='email']")
print("Email Field Placeholder:", email_field.get_attribute("placeholder"))


continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
print("Continue Button Value:", continue_button.get_attribute("value"))


conditions_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use')]")
print("Conditions of Use Link Text:", conditions_link.text)


privacy_notice_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice')]")
print("Privacy Notice Link Text:", privacy_notice_link.text)


need_help_link = driver.find_element(By.XPATH, "//span[contains(text(), 'Need help?')]")
print("Need Help Link Text:", need_help_link.text)


forgot_password_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Forgot your password?')]")
print("Forgot Your Password Link Text:", forgot_password_link.text)


more_ways_to_get_support = driver.find_element(By.XPATH, "//a[contains(text(), 'More ways to get support')]")
print("Other Issues with Sign-In Link Text:", more_ways_to_get_support.text)


create_account_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Create your Amazon account')]")
print("Create Your Amazon Account Button Text:", create_account_button.text)

driver.quit()


#Target


try:

    driver.get("https://www.target.com/")
    sleep(2)


    driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(2)


    driver.find_element(By.XPATH, "//button[@type='button' and @data-test='accountNav-signIn']").click()
    sleep(2)



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

