from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Optional: add waits for better reliability
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

# Konfigurasi opsi Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# Inisialisasi WebDriver dengan opsi yang telah dikonfigurasi
driver = webdriver.Chrome(options=options)

# Open the website
driver.get('https://trensentimen.my.id/login.html')

# Find the username field using its name, css_selector, xpath, or any other supported method
username_field = driver.find_element(By.ID, 'email')  # replace 'username-field-name' with the actual name attribute of the field

# Find the password field using its name, css_selector, xpath, or any other supported method
password_field = driver.find_element(By.ID, 'password')  # replace 'password-field-name' with the actual name attribute of the field

# Find the login button using its name, css_selector, xpath, or any other supported method
login_button = driver.find_element(By.ID, 'button')  # replace 'login-button-name' with the actual name attribute of the button

# Type the username with a delay between each character (simulating typing)
username = 'anjaymemet25@gmail.com'
for character in username:
    username_field.send_keys(character)
    time.sleep(0.01)

# Press Enter key to submit the form
username_field.send_keys(Keys.ENTER)

# Wait for the password field to be visible (you may need to adjust the wait time)
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))

# Type the password with a delay between each character (simulating typing)
password = 'syahid25'
for character in password:
    password_field.send_keys(character)
    time.sleep(0.01)

# Press Enter key to submit the form
password_field.send_keys(Keys.ENTER)

# Wait for the login button to be clickable (you may need to adjust the wait time)
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'button')))

# Click the login button
login_button.click()

sukses_button = WebDriverWait(driver, 10).until(EC.alert_is_present())
# Tangani alert dengan menerima (klik OK)
sukses_button.accept()
time.sleep(5)

# Find the "Daftar Sentimen" button using its xpath
daftar_sentimen_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='sentimen.html']")))

# Click the "Daftar Sentimen" button
daftar_sentimen_button.click()
time.sleep(5)

card = driver.find_element(By.XPATH, "//a[@href='./topik.html?id=660aa0e85066d321df498022']")
card.click()
# Tunggu tombol hapus dapat diklik
delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button is-danger']")))
delete_button.click()

#Alert
sukses_button = WebDriverWait(driver, 10).until(EC.alert_is_present())
# Tangani alert dengan menerima (klik OK)
sukses_button.accept()
time.sleep(5)

# Close the driver
driver.quit()