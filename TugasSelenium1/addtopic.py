from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Konfigurasi opsi Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# Inisialisasi WebDriver dengan opsi yang telah dikonfigurasi
driver = webdriver.Chrome(options=options)

# Maksimalkan jendela browser ke mode layar penuh
driver.maximize_window()

# Open the website
driver.get('https://trensentimen.my.id/login.html')

# Find the username field using its name, css_selector, xpath, or any other supported method
username_field = driver.find_element(By.ID, 'email')  # replace 'username-field-name' with the actual name attribute of the field

# Function to move cursor smoothly to an element and click
def move_cursor_and_click(element):
    element_location = element.location_once_scrolled_into_view
    pyautogui.moveTo(element_location['x'] + 31, element_location['y'] + 150, duration=0.7)
    pyautogui.click()

# Move cursor to username field and click
move_cursor_and_click(username_field)

# Type the username with a delay between each character (simulating typing)
username = 'anjaymemet25@gmail.com'
for character in username:
    username_field.send_keys(character)
    time.sleep(0.01)


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
    time.sleep(0.01)

# Press Enter key to submit the form
password_field.send_keys(Keys.ENTER)

# Wait for the login button to be clickable (you may need to adjust the wait time)
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'button')))

# Move cursor to login button and click
move_cursor_and_click(login_button)

# Alert
sukses_button = WebDriverWait(driver, 10).until(EC.alert_is_present())
# Tangani alert dengan menerima (klik OK)
sukses_button.accept()

# Find the "Daftar Sentimen" button using its xpath
daftar_sentimen_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='sentimen.html']")))

# Move cursor to "Daftar Sentimen" button and click
move_cursor_and_click(daftar_sentimen_button)
time.sleep(3)

# Find the "Tambah Sentimen" button using its ID
add_sentimen_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'showModalButton')))

# Move cursor to "Tambah Sentimen" button and click
move_cursor_and_click(add_sentimen_button)
time.sleep(2)

# Masukkan judul dan topik yang ingin dianalisis
judul_input = driver.find_element(By.ID, "judulInput")
topik_input = driver.find_element(By.ID, "topikInput")
radio_youtube = driver.find_element(By.ID, "radioYoutube")

# Move cursor to password field and click
move_cursor_and_click(judul_input)

# Type the title with a delay between each character (simulating typing)
judul = 'Pengujian Syahid'
for character in judul:
    judul_input.send_keys(character)
    time.sleep(0.05)

# Move cursor to password field and click
move_cursor_and_click(topik_input)

# Type the topic with a delay between each character (simulating typing)
topik = 'Pengujian'
for character in topik:
    topik_input.send_keys(character)
    time.sleep(0.05)

# Select YouTube radio button
# Move cursor to password field and click
move_cursor_and_click(radio_youtube)

# # Wait for the "Simpan" button to be clickable (you may need to adjust the wait time)
# save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'saveModalButton')))

# # Move cursor to "Simpan" button and click
# move_cursor_and_click(save_button)

# Alert
sukses_button = WebDriverWait(driver, 10).until(EC.alert_is_present())
# Tangani alert dengan menerima (klik OK)
sukses_button.accept()

# Wait for a while to see the result (you may adjust the time as needed)
time.sleep(5)

# Close the driver
driver.quit()
