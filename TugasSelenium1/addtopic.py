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

username_field = driver.find_element(By.ID, 'email') 

# Function to move cursor smoothly to an element and click
def move_cursor_and_click(element):
    element_location = element.location_once_scrolled_into_view
    pyautogui.moveTo(element_location['x'] + 31, element_location['y'] + 150, duration=0.7)
    pyautogui.click()

move_cursor_and_click(username_field)

username = 'anjaymemet25@gmail.com'
for character in username:
    username_field.send_keys(character)
    time.sleep(0.01)


username_field.send_keys(Keys.ENTER)

password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))

move_cursor_and_click(password_field)

password = 'syahid25'
for character in password:
    password_field.send_keys(character)
    time.sleep(0.01)

password_field.send_keys(Keys.ENTER)

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'button')))
move_cursor_and_click(login_button)

sukses_button = WebDriverWait(driver, 10).until(EC.alert_is_present())
sukses_button.accept()

daftar_sentimen_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='sentimen.html']")))

move_cursor_and_click(daftar_sentimen_button)
time.sleep(3)

add_sentimen_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'showModalButton')))
move_cursor_and_click(add_sentimen_button)
time.sleep(2)

# Masukkan judul dan topik yang ingin dianalisis
judul_input = driver.find_element(By.ID, "judulInput")
topik_input = driver.find_element(By.ID, "topikInput")
radio_youtube = driver.find_element(By.ID, "radioYoutube")

move_cursor_and_click(judul_input)

judul = 'Pengujian Syahid'
for character in judul:
    judul_input.send_keys(character)
    time.sleep(0.05)

move_cursor_and_click(topik_input)

topik = 'Pengujian'
for character in topik:
    topik_input.send_keys(character)
    time.sleep(0.05)

move_cursor_and_click(radio_youtube)

save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'saveModalButton')))
move_cursor_and_click(save_button)

sukses_button = WebDriverWait(driver, 10).until(EC.alert_is_present())
sukses_button.accept()
time.sleep(5)

# Close the driver
driver.quit()
