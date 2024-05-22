#Amazon Logo
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

#Email Field
driver.find_element(By.ID, 'ap_email')

#Continue Button
driver.find_element(By.ID, 'continue')

#Conditions of Use Link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

#Privacy Notice Link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

#Need Help Link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#Other Issuess with Sign-In Link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

#Create Your Amazon Account Button
driver.find_element(By.ID, 'createAccountSubmit')
