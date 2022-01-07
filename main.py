from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
#You can change sleep seconds up to your connection speed.
driver = webdriver.Firefox()

username = <username>
password = <password>
driver.get("https://instagram.com")
sleep(3)
un = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
un.send_keys(username)
un.send_keys(Keys.RETURN)
sleep(1)
pw = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
pw.send_keys(password)
sleep(1)

sb = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
sb.click()
sleep(10)

pl = driver.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")
pl.click()
sleep(1)

pf = driver.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div")
pf.click()
sleep(10)
fl = driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
fl.click()
sleep(10)
SCROLL_PAUSE = 1
last_height = driver.execute_script("followersbox = document.getElementsByClassName('isgrP')[0];return followersbox.scrollHeight;")
while True:
    driver.execute_script("followersbox = document.getElementsByClassName('isgrP')[0];followersbox.scrollTo(0, followersbox.scrollHeight);")
    sleep(SCROLL_PAUSE)
    new_height = driver.execute_script("followersbox = document.getElementsByClassName('isgrP')[0];return followersbox.scrollHeight;")
    if new_height == last_height:
        break
    last_height = new_height
sleep(10)
following = driver.find_elements(By.CLASS_NAME, "_0imsa")
for person in following:
    print(person.text.upper())
driver.close()
