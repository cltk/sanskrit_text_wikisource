import re
import os 
import string
import regex
import urllib
import sys
from table_scraper import make_dir
from table_scraper import get_html
from table_scraper import write_text
from table_scraper import extract #extract(url,file_name,directory):
try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup

def scrap_link_1(url,file_name,directory):
	html=get_html(url)
	soup = BeautifulSoup(html)
	main_directory=directory+"/"+file_name
	make_dir(main_directory)
	count=0
	for ul in soup.find_all('ul'):
		for li in ul.find_all('li'):
			for a in li.find_all('a'):
					path= "https://sa.wikisource.org"+a['href'] 
					file_name=a.get_text()
					if path[-3:]!="svg":
						count=count+1
						extract(path,file_name,main_directory)

	
#lookinf into each puran main link
def scrap_link(path,inter_directory): 
	url=path
	html=get_html(url)
	soup = BeautifulSoup(html)
	
	count =0


	for ul in soup.find_all('ul')[0:1]:
		for li in ul.find_all('li'):
			for a in li.find_all('a'):
					path= "https://sa.wikisource.org"+a['href'] 
					file_name=a.get_text()
					
					if path[-3:]!="svg":
						count=count+1
						scrap_link_1(path,file_name,inter_directory)
def get_links_books():
	url_list=["https://sa.wikisource.org/wiki/%E0%A4%A8%E0%A4%BE%E0%A4%B0%E0%A4%A6%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D",
	"https://sa.wikisource.org/wiki/%E0%A4%97%E0%A4%B0%E0%A5%81%E0%A4%A1%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D",
	]
	foldernames=["नारदपुराणम्","गरुडपुराणम्"]
	k=1
	url=url_list[k]
	foldername=foldernames[k]
	inter_directory="wiki_doc/puranas_18/"+foldername
	make_dir(inter_directory)  
	scrap_link(url,inter_directory)   
						
						
						 
	
if __name__ == "__main__":
	get_links_books()
	