from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json


#set chrome driver
driver = webdriver.Chrome()
delay = 10

#find link and click
def link_click_by_xpath(link_text, EC_xpath):
	loginElem = driver.find_elements_by_xpath(link_text)

	print(len(loginElem))

	if len(loginElem) > 0:
		loginElem[0].click()

	try:
	    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, EC_xpath)))
	    print("Page is ready!")
	except TimeoutException:
	    print("Loading took too much time!")


def login(username, password):
	#move to instagram home
	driver.get('https://www.instagram.com')
	assert 'Instagram' in driver.title

	#move to login page
	link_click_by_xpath('//div/p/a[contains(@href,"login")]', '//span/button[contains(., "Log in")]')


	#input username, pw
	driver.find_element_by_name('username').send_keys(username)
	driver.find_element_by_name('password').send_keys(password)

	#login
	link_click_by_xpath('//span/button[contains(., "Log in")]', '//input[@placeholder="Search"]')

def explore_tag(tag):
	driver.get('https://www.instagram.com/explore/tags/'+tag)
	source = BeautifulSoup(driver.page_source, 'html.parser')
	
	scripts = source.find_all('script')
	for script in scripts:
		if script.text[:18] == "window._sharedData":
			break	

	data = json.loads(script.contents[0][21:-1])
	print(data)

if __name__ == "__main__":
	explore_tag("seoul")