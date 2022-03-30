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

#def getnextpage(page_soup):
	#page = page_soup.find("table",{"class":"f_fs12 f_fr js_racecard"})
	#if f_fs12 f_fr js_racecard in page:
	#my_url = 'https://racing.hkjc.com/racing/information/Chinese/Racing/LocalResults.aspx?' + str(page.find('a')['href'])


perform = performance[0]
td_list = perform.tbody.find_all("td")
browser.quit()
filename = "test.csv"
f = open(filename, "w")

headers = "rank, number, horsename, ride, train, carry, weight, queue, firsthorse, section1, section2, section3, section4, section5, finishtime, solowin\n"

f.write(headers)


for perform in performance: 

	i=0
	while i<=0:
		i+=1

	rank = td_list[0].text,td_list[12].text,td_list[24].text,td_list[36].text
	number = td_list[1].text.strip(),td_list[13].text.strip(),td_list[25].text.strip(),td_list[37].text.strip()
	horsename = td_list[2].text,td_list[14].text,td_list[26].text,td_list[38].text
	ride = td_list[3].text.strip(),td_list[15].text.strip(),td_list[27].text.strip(),td_list[39].text.strip()
	train = td_list[4].text.strip(),td_list[16].text.strip(),td_list[28].text.strip(),td_list[40].text.strip()
	carry = td_list[5].text,td_list[17].text,td_list[29].text,td_list[41].text
	weight = td_list[6].text,td_list[18].text,td_list[30].text,td_list[42].text
	queue = td_list[7].text,td_list[19].text,td_list[31].text,td_list[43].text
	firsthorse = td_list[8].text,td_list[20].text,td_list[32].text,td_list[44].text
	finishtime = td_list[10].text,td_list[22].text,td_list[34].text,td_list[46].text
	solowin = td_list[11].text,td_list[23].text,td_list[35].text,td_list[47].text
	section_text = td_list[9].get_text(strip=True, separator="\n").split("\n"),td_list[21].get_text(strip=True, separator="\n").split("\n"),td_list[33].get_text(strip=True, separator="\n").split("\n"),td_list[45].get_text(strip=True, separator="\n").split("\n")
	section1 = section_text[0]
	section2 = section_text[1]
	section3 = section_text[2]
	section4 = "N"
	section5 = "N"
	print("section1: " + (str(section1)))
	print("section2: " + (str(section2)))
	print("section3: " + (str(section3)))
	print("section4: " + (str(section4)))
	print("section5: " + (str(section5)))
 
	if ('1400') in racetab.text:
		section4 = section_text[3]

	if ('1600') in racetab.text:
		section4 = section_text[3]

	if ('1650') in racetab.text:
		section4 = section_text[3]

	if ('1800') in racetab.text:
		section4 = section_text[3]
		section5 = section_text[4]



	f.write(str(rank[i]) + "," +str(number) + "," +str(horsename) + "," +str(ride) + "," +str(train) + "," +str(carry) + "," +str(weight) + "," +str(queue) + "," +str(firsthorse) + "," +str(section1) + "," +str(section2) + ","  +str(section3) + "," +str(section4) + "," +str(section5) + "," +str(finishtime) + "," +str(solowin) + "\n")



	print("rank: " + rank[i])
	print("number: " + str(number))
	print("horsename: " + str(horsename))
	print("ride: " + str(ride))
	print("train: " + str(train))
	print("carry: " + str(carry))
	print("weight: " + str(weight))
	print("queue: " + str(queue))
	print("firsthorse: " + str(firsthorse))
	print("finishtime: " + str(finishtime))
	print("solowin: " + str(solowin))

	
	

f.close