from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium_dict_file import * 

data_dict = {}
driver = webdriver.Chrome('/Users/justinding/Desktop/Summer-2021/spider/scrapy/LinkedIn/chromedriver')
driver.get('https://www.linkedin.com')


### Log in 
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys('justin.qizhen.ding@gmail.com')
password.send_keys('plungein12')

submit = driver.find_element_by_xpath("//button[@type='submit']").click() 

### scrapping part

driver.get('https://www.linkedin.com/jobs/search/')
element = driver.find_elements_by_xpath("//ul[@class='jobs-search-results__list list-style-none']//a[@class='disabled ember-view job-card-container__link job-card-list__title']")
time.sleep(3)
# element.location_once_scrolled_into_view
for item in element:
	time.sleep(5)
	print(item.text)
	# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	time.sleep(5)
	driver.find_element_by_link_text(item.text).click()
	time.sleep(3)
	des= driver.find_element_by_xpath("//div[@class='jobs-box__html-content jobs-description-content__text t-14 t-normal']")
	print(des.text)
	data_dict[item.text] = des.text
driver.quit()

if __name__ == "__main__":
	data_store(data_dict)
