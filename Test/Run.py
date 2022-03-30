import bs4
from bs4 import BeautifulSoup as soup
import time  
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
browser = webdriver.Firefox()
my_url = 'https://racing.hkjc.com/racing/information/Chinese/Racing/LocalResults.aspx?RaceDate=2021/09/15&Racecourse=HV&RaceNo=3'
browser.get(my_url) 
time.sleep(5)

page_soup = soup(browser.page_source, "html.parser")
performance = page_soup.findAll("div",{"class":"performance"})
race = page_soup.find("div",{"class":"race_tab"})
raceselect = race.select("td")
racetab = raceselect[6]
ground = raceselect[8]
road = raceselect[11]

perform = performance[0]
td_list = perform.tbody.find_all("td")
browser.quit()
filename = "test.csv"
f = open(filename, "w")

headers = "rank, number, horsename, ride, train, carry, weight, queue, firsthorse, section1, section2, section3, section4, section5, finishtime, solowin\n"

f.write(headers)


for perform in performance:
	rank = td_list[0].text
	number = td_list[1].text.strip()
	horsename = td_list[2].text
	ride = td_list[3].text.strip()
	train = td_list[4].text.strip()
	carry = td_list[5].text
	weight = td_list[6].text
	queue = td_list[7].text
	firsthorse = td_list[8].text
	finishtime = td_list[10].text
	solowin = td_list[11].text
	section_text = td_list[9].get_text(strip=True, separator="\n").split("\n")
	section1 = section_text[0]
	section2 = section_text[1]
	section3 = section_text[2]
	section4 = "N"
	section5 = "N"
	print("section1: " + section1)
	print("section2: " + section2)
	print("section3: " + section3)
	print("section4: " + section4)
	print("section5: " + section5)	
	
	if ('1400') in racetab.text:
		section4 = section_text[3]
	if ('1600') in racetab.text:
		section4 = section_text[3]
	if ('1650') in racetab.text:
		section4 = section_text[3]
	if ('1800') in racetab.text:
		section4 = section_text[3]
		section5 = section_text[4]

	
