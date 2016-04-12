import re
import os 
import string
import regex
import urllib
#import urllib.request
import sys
from table_scraper import make_dir
from table_scraper import get_html
from table_scraper import write_text
from table_scraper import extract #extract(url,file_name,directory):
try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup

def get_links_books():
	url_list=["https://sa.wikisource.org/wiki/%E0%A4%AC%E0%A5%8D%E0%A4%B0%E0%A4%B9%E0%A5%8D%E0%A4%AE%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D",
	"https://sa.wikisource.org/wiki/%E0%A4%B5%E0%A4%BE%E0%A4%AE%E0%A4%A8%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D",
	"https://sa.wikisource.org/wiki/%E0%A4%85%E0%A4%97%E0%A5%8D%E0%A4%A8%E0%A4%BF%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D",
	"https://sa.wikisource.org/wiki/%E0%A4%A8%E0%A4%BE%E0%A4%B0%E0%A4%A6%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D-_%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%B5%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%A7%E0%A4%83",
	"https://sa.wikisource.org/wiki/%E0%A4%AE%E0%A4%A4%E0%A5%8D%E0%A4%B8%E0%A5%8D%E0%A4%AF%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D",
	"https://sa.wikisource.org/wiki/%E0%A4%B5%E0%A4%B0%E0%A4%BE%E0%A4%B9%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D",
	"https://sa.wikisource.org/wiki/%E0%A4%A8%E0%A4%BE%E0%A4%B0%E0%A4%A6%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D-_%E0%A4%89%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%B0%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%A7%E0%A4%83"
	,"https://sa.wikisource.org/wiki/%E0%A4%AC%E0%A5%8D%E0%A4%B0%E0%A4%B9%E0%A5%8D%E0%A4%AE%E0%A4%B5%E0%A5%88%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%A4%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D",
	"https://sa.wikisource.org/wiki/%E0%A4%B5%E0%A4%BE%E0%A4%AF%E0%A5%81%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D/%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%B5%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%A7%E0%A4%AE%E0%A5%8D"
	,"https://sa.wikisource.org/wiki/%E0%A4%B5%E0%A4%BE%E0%A4%AF%E0%A5%81%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D/%E0%A4%89%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%B0%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%A7%E0%A4%AE%E0%A5%8D"]

	foldernames=["","ब्रह्मपुराणम्","वामनपुराणम्","अग्निपुराणम्","मत्स्यपुराणम्","वराहपुराणम्","नारदपुराणम्","ब्रह्मवैवर्तपुराणम्","वायुपुराणम्","उत्तरार्धम्"]
	k=9
	url=url_list[k]
	foldername=foldernames[k]
	html=get_html(url)
	soup = BeautifulSoup(html)
	
	directory="wiki_doc/puranas_18/"+foldername
	make_dir(directory)
	count=0
	table_count=0
	for tables in soup.find_all('table')[2:3]:
		print (table_count)
		for trs in tables.find_all('tr'):
			for tds in trs.find_all('td'):
				for a in tds.findAll('a'):
					print (a.get_text())
					if a['href'][-1]!="1":
						extract("https://sa.wikisource.org"+a['href'],a.get_text(),directory)
						count=count+1
		table_count=table_count+1			
	print (count)			

def get_links_books_type2():
	url_list=["https://sa.wikisource.org/wiki/%E0%A4%97%E0%A4%B0%E0%A5%81%E0%A4%A1%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D/%E0%A4%AC%E0%A5%8D%E0%A4%B0%E0%A4%B9%E0%A5%8D%E0%A4%AE%E0%A4%95%E0%A4%BE%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A4%83_(%E0%A4%AE%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%95%E0%A4%BE%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A4%83)",
	"https://sa.wikisource.org/wiki/%E0%A4%97%E0%A4%B0%E0%A5%81%E0%A4%A1%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A5%87%E0%A4%A4%E0%A4%95%E0%A4%BE%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A4%83_(%E0%A4%A7%E0%A4%B0%E0%A5%8D%E0%A4%AE%E0%A4%95%E0%A4%BE%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A4%83)"
	,"https://sa.wikisource.org/wiki/%E0%A4%B2%E0%A4%BF%E0%A4%99%E0%A5%8D%E0%A4%97%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D_-_%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%B5%E0%A4%AD%E0%A4%BE%E0%A4%97%E0%A4%83"
	,"https://sa.wikisource.org/wiki/%E0%A4%B2%E0%A4%BF%E0%A4%99%E0%A5%8D%E0%A4%97%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D_-_%E0%A4%89%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%B0%E0%A4%AD%E0%A4%BE%E0%A4%97%E0%A4%83"]

	foldernames=["ब्रह्मकाण्डः_(मोक्षकाण्डः)","प्रेतकाण्डः_(धर्मकाण्डः)","लिङ्गपुराणम्_-_पूर्वभागः","लिङ्गपुराणम्_-_उत्तरभागः"]
	k=2
	url=url_list[k]
	foldername=foldernames[k]
	html=get_html(url)
	soup = BeautifulSoup(html)
	
	directory="wiki_doc/puranas_18/"+foldername
	make_dir(directory)
	count=0

	table_count=0
	for tables in soup.find_all('table')[1:2]:
		print (table_count)
		for trs in tables.find_all('tr'):
			for tds in trs.find_all('td'):
				for a in tds.findAll('a'):
					print (a.get_text())
					if a['href'][-1]!="1":
						extract("https://sa.wikisource.org"+a['href'],a.get_text(),directory)
						count=count+1
		table_count=table_count+1			
	print (count)				
if __name__ == "__main__":
	get_links_books()
	#get_links_books_type2()