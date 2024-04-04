from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

# Konfigurasi opsi Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# Inisialisasi WebDriver dengan opsi yang telah dikonfigurasi
driver = webdriver.Chrome(options=options)

# Maksimalkan jendela browser ke mode layar penuh
driver.maximize_window()

# Open the website
driver.get('https://trensentimen.my.id/register.html')

# Find the username field using its name, css_selector, xpath, or any other supported method
name_field = driver.find_element(By.ID, 'name')  # replace 'username-field-name' with the actual name attribute of the field

# Find the username field using its name, css_selector, xpath, or any other supported method
username_field = driver.find_element(By.ID, 'email')  # replace 'username-field-name' with the actual name attribute of the field

# Find the password field using its name, css_selector, xpath, or any other supported method
password_field = driver.find_element(By.ID, 'password')  # replace 'password-field-name' with the actual name attribute of the field

no_wa_field = driver.find_element(By.ID, 'nohp')

confirm_password_field = driver.find_element(By.ID, 'confirm-password')  # replace 'password-field-name' with the actual name attribute of the field

# Find the login button using its name, css_selector, xpath, or any other supported method
register_button = driver.find_element(By.ID, 'button')  # replace 'login-button-name' with the actual name attribute of the button

# Function to move cursor smoothly to an element and click
def move_cursor_and_click(element):
    element_location = element.location_once_scrolled_into_view
    pyautogui.moveTo(element_location['x'] + 30, element_location['y'] + 160, duration=0.7)
    pyautogui.click()

# Move cursor to name field and click
move_cursor_and_click(name_field)

# Type the name with a delay between each character (simulating typing)
name = 'Syahid'
for character in name:
    name_field.send_keys(character)
    time.sleep(0.05)

# Press Enter key to submit the form
name_field.send_keys(Keys.ENTER)

# Move cursor to username field and click
move_cursor_and_click(username_field)

# Type the username with a delay between each character (simulating typing)
username = 'anjaymemet25@gmail.com'
for character in username:
    username_field.send_keys(character)
    time.sleep(0.05)

# Press Enter key to submit the form
username_field.send_keys(Keys.ENTER)

# Wait for the password field to be visible (you may need to adjust the wait time)
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))

# Move cursor to password field and click
move_cursor_and_click(password_field)

# Type the password with a delay between each character (simulating typing)
password = 'syahid25'
for character in password:
    password_field.send_keys(character)
    time.sleep(0.05)

# Press Enter key to submit the form
password_field.send_keys(Keys.ENTER)

# Move cursor to no_wa field and click
move_cursor_and_click(no_wa_field)

# Type the no_wa with a delay between each character (simulating typing)
no_wa = '6285784718312'
for character in no_wa:
    no_wa_field.send_keys(character)
    time.sleep(0.05)

# Press Enter key to submit the form
no_wa_field.send_keys(Keys.ENTER)

# Wait for the confirm password field to be visible (you may need to adjust the wait time)
confirm_password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'confirm-password')))

# Move cursor to confirm password field and click
move_cursor_and_click(confirm_password_field)

# Type the password with a delay between each character (simulating typing)
confirm_password = 'syahid25'
for character in password:
    confirm_password_field.send_keys(character)
    time.sleep(0.05)

# Press Enter key to submit the form
confirm_password_field.send_keys(Keys.ENTER)

# Wait for the register button to be clickable (you may need to adjust the wait time)
# register_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'button')))

# # Move cursor to register button and click
# move_cursor_and_click(register_button)

# # Close the driver
# driver.quit()
