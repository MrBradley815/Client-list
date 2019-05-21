from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

then = time.time()
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 20)
login = '83451:233428'
password = 'Lunch4bl35'

driver.get("https://www.sagemember.com")
assert "SAGEmember.com" in driver.title

elem = driver.find_element_by_class_name("form-control")
elem.send_keys(login)
elem = driver.find_element_by_id("password")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "More information")))
driver.find_element_by_xpath("//ul[@id='side-menu']/li[2]/a").click()

wait.until(EC.frame_to_be_available_and_switch_to_it('ContentFrame'))
driver.find_element_by_xpath("//table[@id='coStoreList']/tbody/tr[2]/td[7]/form/a").click()

driver.switch_to.default_content()

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Clients")))
driver.find_element_by_xpath("//ul[@id='side-menu']/li[4]/ul/li[5]/a").click()

wait.until(EC.frame_to_be_available_and_switch_to_it('ContentFrame'))

clients = driver.find_element_by_xpath("//html/body/div[2]/table/tbody/tr[1]")
while(clients):
	driver.find_element_by_xpath("//html/body/div[2]/table/tbody/tr[1]/td[6]/input[3]").click()
	driver.switch_to.alert.accept()
	wait.until(EC.element_to_be_clickable((By.XPATH, "//input[text()='Delete']")))
	clients = driver.find_element_by_xpath("//html/body/div[2]/table/tbody/tr[1]")

now = time.time()

print("It took: ", (now-then)/60, " minutes")








