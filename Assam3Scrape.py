c1 = "entry-content"
from selenium import webdriver
from selenium.webdriver.common.by import By
from numpy import unique
import os
driver = webdriver.Firefox()
#t = int(input())
t = 0
URLS = open(f"NLP/fullurls3_block_{t}.txt",'r').read().split("\n")
URLS = unique(URLS)
try:os.mkdir(r"NLP/Assam3/urls_{t}")
except:pass
for i,url in enumerate(URLS):
    driver.get(url)
    try:
        dis = driver.find_elements(By.ID,'dismiss-button')
        dis = dis[0]
        dis.click()
    except:pass
    D = driver.find_elements(By.CLASS_NAME,c1)
    s = [d.text for d in D]
    s = "\n".join(s)
    f = open(f"NLP/Assam3/urls_{t}/data_{i}.txt",'w')
    f.write(s)
    f.close()
driver.close()