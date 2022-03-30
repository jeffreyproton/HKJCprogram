import bs4
from bs4 import BeautifulSoup as soup
import time  
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from requests_html import HTMLSession

options = Options()
options.headless = True
browser = webdriver.Firefox()
my_url = 'https://racing.hkjc.com/racing/information/CHINESE/Racing/ResultsAll.aspx?RaceDate=2021/09/15'
browser.get(my_url) 
time.sleep(5)

page_soup = soup(browser.page_source, "html.parser")

browser.quit()
filename = "test.csv"
f = open(filename, "w")


headers = "rank, horsename, ride, train, carry, queue\n"

f.write(headers)

race = page_soup.select("div.bg_blue.color_w.f_fs13.font_wb div")

for racet in race:
	