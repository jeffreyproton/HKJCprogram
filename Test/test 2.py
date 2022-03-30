import time  
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
browser = webdriver.Firefox()
my_url = 'https://racing.hkjc.com/racing/information/Chinese/Racing/LocalResults.aspx?RaceDate=2021/09/12&Racecourse=ST&RaceNo=1'
browser.get(my_url) 
time.sleep(5)
 
browser.quit()
