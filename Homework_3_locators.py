# Amazon Logo
from selenium.webdriver.common.by import By

driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']")

# Create account
driver.find_element(By.CSS_SELECTOR, "h1[class='a-spacing-small']")

# Your Name input field
driver.find_element(By.ID, 'ap_customer_name')

# Your Email input field
driver.find_element(By.ID, 'ap_email')

# Password input field
driver.find_element(By.ID, 'ap_password')

# Password must be at least 6 characters
# Part 1 - this is just the i before the text
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-alert")
# Part 2 - text: Password must be at least 6 characters
driver.find_element(By.CSS_SELECTOR, "div.a-alert-content")

# Re-enter password
driver.find_element(By.ID, 'ap_password_check')

# Create your Amazon account is not the text in my input field
# The text in that field for me says Continue. I will write it for that rather thank skip
driver.find_element(By.ID, 'continue')

# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")

# Privacy Notice
# by adding the word notification, it narrowed it down to 1 result
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_privacy_notice']")

# Sign in
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")







