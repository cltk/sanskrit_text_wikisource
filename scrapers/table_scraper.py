import re
import os 
import string
import regex
import urllib
import urllib.request
import sys
try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup
def make_dir(directory):
	if not os.path.exists(directory):
			os.makedirs(directory)  
def get_html(url_link):
	if sys.version_info < (3, 4):
			return urllib.urlopen(url_link)
	else:
		with urllib.request.urlopen(url_link) as url:
			return url.read()
def encode(line):
	if sys.version_info < (3, 3):
			return line
	else:
			line.encode('utf-8')

def write_text(lines,target):
	no_sentences=0
	for l in range(len(lines)):
				line=lines[l]
				#line=line.strip()

				if line!="":
					target.write(line)
					target.write("\n")
					no_sentences+=1
	return no_sentences

def extract(url,file_name,directory):
	html=get_html(url)
	soup = BeautifulSoup(html)
	#print directory
	#print (file_name).encode('utf-8')
	path_=directory+"/"+file_name+".txt"
	
	target_= open(path_, 'w')

	text=soup.findAll('p')

	for i in range (0,len(text)):
		if text[i]!="":
			line=text[i].get_text()
			if  line.rstrip():
				
				target_.write(line.strip())
				target_.write("\n")

def scrap_link_1(url,file_name,directory):
	html=get_html(url)
	soup = BeautifulSoup(html)
	#print directory
	#print (file_name).encode('utf-8')
	main_directory=directory+"/"+file_name
	make_dir(main_directory)
	#print main_directory ,"ss",url.encode('utf-8')
	count=0
	for ul in soup.find_all('ul')[1:2]:
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
	print ("scraping")
	count =0

	for ul in soup.find_all('ul')[0:1]:
		for li in ul.find_all('li'):
			for a in li.find_all('a'):
					path= "https://sa.wikisource.org"+a['href'] 
					file_name=a.get_text()
					#print   ("inter_directory",(file_name[:-2])
					#print   (file_name[:-2]=="अध्यायः")
					if path[-3:]!="svg":
							count=count+1
							scrap_link_1(path,file_name,inter_directory)
#finding 18 puran books                        
def get_links_books():
	main_directory="wiki_doc1"
	make_dir(main_directory)
	url="https://sa.wikisource.org/wiki/%E0%A4%AE%E0%A5%81%E0%A4%96%E0%A4%AA%E0%A5%81%E0%A4%9F%E0%A4%AE%E0%A5%8D"
	html=get_html(url)
	soup = BeautifulSoup(html)
	
	count =0
	doc_name="/puranas_18/"
	for tables in soup.find_all('table')[12:13]:
		for trs in tables.find_all('tr'):
			for tds in trs.find_all('td')[0:1]:
				for a in tds.findAll('a')[0:1]:
					path= "https://sa.wikisource.org"+a['href'] 
					folder_name=a.get_text()
					if path[-3:]!="svg":
						count=count+1
						inter_directory=main_directory+doc_name+folder_name   
						make_dir(inter_directory)
						scrap_link(path,inter_directory)    
	
if __name__ == "__main__":
	get_links_books()
	