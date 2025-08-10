from selenium import webdriver
from selenium.webdriver.common.by import By
f = open("NLP/last_url.txt",'r')
s = f.read()
f.close()
s = s.split("\n")
url = s[0]
i = int(s[1]) -1
print("starting from i=",i,"at",url)
from huggingface_hub import HfApi
api = HfApi(token="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")
def upload(I,DID,Api):
  Api.upload_file(
      path_or_fileobj=f"NLP/Assam2/data_{I}_{DID}.txt",
      path_in_repo=f"data_{I}_{DID}.txt",
      repo_id="iksmstuff/assam_neonow_in_corpus",
      repo_type="dataset",
  )
#latest article
driver = webdriver.Firefox()
while True:
  driver.get(url)
  D = driver.find_elements(By.CLASS_NAME,"post-wrapper")[0]
  D = D.find_elements(By.CLASS_NAME,"post-wrap")
  s = ""
  prev = None
  data_id = "unkid"
  for d in D:
      text = d.find_elements(By.CLASS_NAME,'content-inner')
      for t in text: s += t.text + "\n"
      try:prev =  d.get_attribute("data-prev")
      except:pass
      try:data_id = d.get_attribute("data-id")
      except:pass
  i += 1
  f = open(f"NLP/Assam2/data_{i}_{data_id}.txt",'w')
  f.write(s)
  f.close()
  f = open(f"NLP/last_url.txt",'w')
  f.write(url + "\n" + str(i))
  f.close()
  upload(i,data_id,api)
  if prev is None:
    print("data-prev isn't here for this link : " + url)
    break
  else:
    url = prev
driver.close()