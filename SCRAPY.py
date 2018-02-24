from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
import os

os.system('cls')
 
driver = webdriver.PhantomJS()
driver.get('https://duckduckgo.com/?q=porn&t=hg&ia=web')
 
lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser') # parse the html using beautiful soup and store in variable 'soup'
for link in soup.find_all('a'):
    print(link.get('href'))