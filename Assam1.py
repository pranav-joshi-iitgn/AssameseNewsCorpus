import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
urls = open("NLP/URLS1.txt").read().split("\n")
driver = webdriver.Firefox()
for i in range(len(urls)):
    driver.get(urls[i])
    time.sleep(1)
    B = driver.find_elements(By.ID,'dismiss-button')
    if len(B):
        B[0].click()
        time.sleep(1)
    Art = driver.find_elements(By.TAG_NAME,"article")
    Art = [art for art in Art if art.get_attribute("class")=="blog-post hentry item-post"]
    CONTENT = []
    for art in Art:
        D = art.find_element(By.ID,'post-body')
        Floating = D.text.split("\n")
        Floating = [x for x in Floating if x]
        Floating = "\n".join(Floating)
        #Paras = D.find_elements(By.TAG_NAME,'p')
        #Paras = [P.text.strip() for P in Paras]
        #Paras = [P for P in Paras if P]
        #Spans = D.find_elements(By.TAG_NAME,'span')
        #Spans = [P.text.strip() for P in Spans]
        #Spans = [P for P in Spans if P]
        #Content = Paras + Spans
        #Content.append(Floating)
    CONTENT.append(Floating)
    f = open(f"NLP/Assam1/data_{i}.txt",'w')
    f.write("\n".join(CONTENT))
    f.close()
    print(f"Link {i} done. {len(urls) - (i+1)} left to do.")
driver.close()