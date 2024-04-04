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

# Open YouTube
driver.get('https://trensentimen.my.id/login.html')

# Find the username field using its name, css_selector, xpath, or any other supported method
username_field = driver.find_element(By.ID, 'email')  # replace 'username-field-name' with the actual name attribute of the field

# Find the password field using its name, css_selector, xpath, or any other supported method
password_field = driver.find_element(By.ID, 'password')  # replace 'password-field-name' with the actual name attribute of the field

# Find the login button using its name, css_selector, xpath, or any other supported method
login_button = driver.find_element(By.ID, 'button')  # replace 'login-button-name' with the actual name attribute of the button

# Function to move cursor smoothly to an element and click
def move_cursor_and_click(element):
    element_location = element.location_once_scrolled_into_view
    pyautogui.moveTo(element_location['x'] + 30 , element_location['y'] + 160 , duration=0.7)
    pyautogui.click()

# Move cursor to username field and click
move_cursor_and_click(username_field)

# Type the username with a delay between each character (simulating typing)
username = 'anjaymemet25@gmail.com'
for character in username:
    username_field.send_keys(character)
    time.sleep(0.01)

# Move cursor to password field and click
move_cursor_and_click(password_field)

# Type the password with a delay between each character (simulating typing)
password = 'syahid25'
for character in password:
    password_field.send_keys(character)
    time.sleep(0.01)

# Move cursor to login button and click
move_cursor_and_click(login_button)

# Alert
sukses_button = WebDriverWait(driver, 10).until(EC.alert_is_present())
# Tangani alert dengan menerima (klik OK)
sukses_button.accept()

# close driver
# driver.quit()
