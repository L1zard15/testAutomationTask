from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# https://the-internet.herokuapp.com/login credintials
username = "username"
password = "password"
# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
# head to website login page
driver.get("https://the-internet.herokuapp.com/login")
# find username/email field and send the username itself to the input field
driver.find_element_by_id("username").send_keys(username)
# find password input field and insert password as well
driver.find_element_by_id("password").send_keys(password)
# click login button
driver.find_element_by_name("Login").click()
# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements_by_class_name("flash error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
    # close the driver
driver.close()