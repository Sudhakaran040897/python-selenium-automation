from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#Amazon
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
sleep(2)

#
amazon_logo = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")


if amazon_logo:
    print("Amazon logo found!")
else:
    print("Amazon logo not found.")

create_account = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")

if create_account:
    print("Create account found!")
else:
    print("Create account not found.")

first_and_last_name = driver.find_element(By.XPATH, "//input[@placeholder='First and last name']")
if first_and_last_name:
    print("First name and last name found!")
else:
    print("First name and last name not found.")

email = driver.find_element(By.XPATH, "//input[@aria-describedby ='ap_email_context_message_section emailPhoneNumberAlert']")
if email:
    print("Email address found!")
else:
    print("Email address not found.")

password = driver.find_element(By.XPATH, "//input[@autocomplete='new-password']")
if password:
    print("Password found!")
else:
    print("Password not found.")
re_enter_password = driver.find_element(By.XPATH,"//input[@name='passwordCheck']")
if re_enter_password:
    print("Password found!")
else:
    print("Password not found.")

continue_button = driver.find_element(By.XPATH, "//input[@type='submit']")
if continue_button:
    print("Continue button found!")
else:
    print("Continue button not found.")

conditions_link = driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
if conditions_link:
    print("Condition link found!")
else:
    print("Condition link not found.")

privacy_note = driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")
if privacy_note:
    print("Privacy note found!")
else:
    print("Privacy note not found.")

sign_in = driver.find_element(By.XPATH, "//a[@class='a-link-emphasis']")
if sign_in:
    print("Signin found!")
else:
    print("Sign in not found.")

driver.quit()



#Target_1

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.target.com/")
sleep(2)

cart_icon = driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']")
cart_icon.click()
sleep(2)

empty_cart_message = driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 dtCtuk']")
print("Message found: ", empty_cart_message.text)
assert "Your cart is empty" in empty_cart_message.text

driver.quit()

#Target_2


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.target.com/")
sleep(2)

sign_in = driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']")
sign_in.click()
sleep(2)

sign_in_2 = driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
sign_in_2.click()
sleep(2)

page_confirmation = driver.find_element(By.XPATH, "//h1/span[contains(text(), 'Sign into your Target account')]").text
if page_confirmation:
    print(f"Page confirmation found:{page_confirmation}")
else:
    print("Page confirmation not found.")

driver.quit()


