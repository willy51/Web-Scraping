import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import csv

#on utilise cette methode car le raw Html il n'y a que [<span id="country-code"></span>]
#On utilise Browser puisque youtube est une page dynamique donc BS4 n arrive pas a recuperer les donnes 
Browser = webdriver.Chrome()
Browser.get('https://www.youtube.com')
#youtu home page


time.sleep(5)
#Cokies
btn =Browser.find_element(By.CSS_SELECTOR,".yt-spec-button-shape-next.yt-spec-button-shape-next--filled.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--enable-backdrop-filter-experiment")
btn.click()
time.sleep(3)
#Quest 1

spans =Browser.find_elements(By.CSS_SELECTOR,'span')
time.sleep(2)
for span in spans:
    print(span.text) 

print(len(spans))
#Quest2
imgs=Browser.find_elements(By.CSS_SELECTOR,'img')
print("nb d'image sur l'home page "+ str(len(imgs)))
time.sleep(5)


#Quest3 
#Part1
button= Browser.find_element(By.CSS_SELECTOR,"#guide-button")
button.click()
time.sleep(5)
links = Browser.find_elements(By.CSS_SELECTOR, '.yt-simple-endpoint.style-scope.ytd-guide-entry-renderer')
j =0
while j < len (links):
    if links[j].get_attribute("title")=="Musique":
        print("The url for the Musique  "+links[j].get_attribute("href"))
    elif links[j].get_attribute("title")=="Sport":
        print("The url for the Sport  "+links[j].get_attribute("href"))
    j=j +1

#Part2
Browser.get('https://www.youtube.com/results?search_query=stairway+to+heaven')
time.sleep(5)
Vids =Browser.find_elements(By.CSS_SELECTOR,'#video-title')
print(len(Vids))
i = 0
while i<3 :
    print(Vids[i].text)
    i=i+1
time.sleep(2)

#part3
Browser.get('https://www.youtube.com/watch?v=qHFxncb1gRY')
time.sleep(10)
Descri_Video=Browser.find_element(By.CSS_SELECTOR,'.yt-core-attributed-string--link-inherit-color')
RealetedUrl=Browser.find_elements(By.CSS_SELECTOR,'.yt-simple-endpoint.style-scope.ytd-compact-video-renderer')
RealetedVidTitle = Browser.find_elements(By.CSS_SELECTOR,'#video-title')
ReletedVidNbVue =Browser.find_elements(By.CSS_SELECTOR,'.inline-metadata-item.style-scope.ytd-video-meta-block')
ReletedVidDur =Browser.find_elements(By.CSS_SELECTOR,'.badge-shape-wiz__text')


print ("Description de la video: "+Descri_Video.text)

i = 0
while i<len(RealetedUrl) :
    if i<1:
     print( RealetedVidTitle[i].text+" "+str(ReletedVidNbVue[i].text)+" "+ReletedVidDur[i].text+" "+RealetedUrl[i].get_attribute('href'))
    else:
        j=2*i
        print( RealetedVidTitle[i].text+" "+str(ReletedVidNbVue[j].text)+" "+ReletedVidDur[i].text +" "+RealetedUrl[i].get_attribute('href'))
    i=i+1

time.sleep(70)