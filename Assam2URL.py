tags = [
"মুখ্যপৃষ্ঠা",
"অসম",
"নৰ্থ-ইষ্ট",
"প্ৰতিৱেশী",
"অভিমত",
"ক্ৰীড়া",
"বাণিজ্য",
"সংস্কৃতি",
"ভাষা-সাহিত্য",
"যুৱ-কণ্ঠ",
"শিক্ষা",
"জীৱনশৈলী",
"প্ৰযুক্তি",
"মনোৰঞ্জন",
"প্ৰাসংগিক প্ৰশ্ন",
"স্বাস্থ্য",
"ফেচবুক কৰ্ণাৰ",
]

JS_code = [
"c = 'jeg_block_navigation'",
"D = document.getElementsByClassName(c)[12]",
"A = D.children[1]",
"A = A.children[0]",
"Int = setInterval(function(){window.scroll(0,document.body.scrollHeight)},500)",
"k = setInterval(function(){A.click()},500)",
"L=[];for(var i=0;i<6000;i++){art = Arts[i];L[i] = art.children[art.children.length -1].children[0].children[0].href }",
"document.getElementsByTagName('article').length",
]

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from numpy import unique

base_url = "https://assam.nenow.in/"
driver = webdriver.FireFox()
driver.get(base_url)
time.sleep(1)
driver.execute_script(JS_code[0])
driver.execute_script(JS_code[1])
driver.execute_script(JS_code[2])
driver.execute_script(JS_code[3])
driver.execute_script(JS_code[4])
driver.execute_script(JS_code[5])
for i in range(7*12): #7 hours !
    time.sleep(300) #wait 5 minutes
    Arts = driver.find_elements(By.TAG_NAME,"article")
    Artlinks = []
    for art in Arts:
        div = art.find_elements(By.TAG_NAME,'div')[-1]
        anc = div.find_elements(By.TAG_NAME,'a')[0]
        Artlinks.append(anc.href)
    Artlinks = unique(Artlinks)
    f = open("NLP/Data_Assam2.txt",'w')
    f.write("\n".join(Artlinks))
    f.close()



