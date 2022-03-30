import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

from selenium import webdriver
import time  


browser = webdriver.Firefox()  
my_url = 'https://racing.hkjc.com/racing/information/Chinese/Racing/LocalResults.aspx?RaceDate=2021/09/12&Racecourse=ST&RaceNo=1'
browser.get(my_url)  


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#grab all table
Table = page_soup.findAll("div",{"class":"localResults commContent fontFam"})
performance = page_soup.findAll("div",{"class":"performance"})

perform = performance[0]
perform.find_all("td")

filename = "test.csv"
f = open(filename, "w")

headers = "rank, number, horsename, ride, train, carry, weight, queue, firsthorse, position, finishtime, solowin\n"

f.write(headers)

for perform in performance:
	td_list = perform.tbody.find_all("td")
	rank = td_list[0].text.strip()
	number = td_list[1].text.strip()
	horsename = td_list[2].text.strip()
	ride = td_list[3].text.strip()
	train = td_list[4].text.strip()
	carry = td_list[5].text.strip()
	weight = td_list[6].text.strip()
	queue = td_list[7].text.strip()
	firsthorse = td_list[8].text.strip()
	position = td_list[9].text.strip()
	finishtime = td_list[10].text.strip()
	solowin = td_list[11].text.strip()

	print("rank: " + rank)
	print("number: " + number)
	print("horsename: " + horsename)
	print("ride: " + ride)
	print("train: " + train)
	print("carry: " + carry)
	print("weight: " + weight)
	print("queue: " + queue)
	print("firsthorse: " + firsthorse)
	print("position: " + position)
	print("finishtime: " + finishtime)
	print("solowin: " + solowin)

	f.write(rank + "," +number + "," +horsename + "," +ride + "," +train + "," +carry + "," +weight + "," +queue + "," +firsthorse + "," +position + "," +finishtime + "," +solowin + "\n")
	
f.close