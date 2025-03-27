from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 
import csv
import os
import requests

os.chdir(os.path.dirname(os.path.abspath(__file__)))

Browser = webdriver.Chrome()
Browser.get('https://www.nba.com/stats/players')        

time.sleep(2)
try:
    cookies = Browser.find_element(By.CSS_SELECTOR,"#onetrust-accept-btn-handler")
    cookies.click()
except:
    pass
time.sleep(2)

allPla = Browser.find_element(By.CSS_SELECTOR,".Block_blockAd__1Q_77")
allPla.click()

time.sleep(6)

table = Browser.find_elements(By.CSS_SELECTOR,".DropDown_select__4pIg9")[5]

selectPage = Select(table)
selectPage.select_by_index(0)


tablePlayer = Browser.find_elements(By.CSS_SELECTOR,".Crom_table__p1iZz")
lst = tablePlayer[0].text.split("\n")
for i in range(0,len(lst)):
    lst[i] = lst[i].split(" ")
    for j in range(0,len(lst[i])):
        lst[i][j] = lst[i][j].replace(",","")

time.sleep(2)

tableId = Browser.find_element(By.CSS_SELECTOR,".Crom_body__UYOcU").find_elements(By.CSS_SELECTOR,".Anchor_anchor__cSc3P")

image = []
for i in tableId:
    if "player" in i.get_attribute("href"):
        image = image + ["https://cdn.nba.com/headshots/nba/latest/1040x760/"+str(i.get_attribute("href").split("/")[-2])+".png"]

for i in range(1, len(lst)):
    lst[i] = [image[i-1]] + lst[i]
    if len(lst[i]) > 24:
        lst[i][2] = " ".join(lst[i][2:len(lst[i]) - 21])
        del lst[i][3:len(lst[i]) - 21]

Browser.quit()

lst[0] = ["Image"] + lst[0]
with open('NBA.csv', 'w', newline='', encoding='utf-16') as file:
    writer = csv.writer(file)
    for row in lst:
        if len(row) > 1:  
            writer.writerow(row)


image_dir = "NBA_Player_Images"
if not os.path.exists(image_dir):
    os.makedirs(image_dir)


for idx, img_url in enumerate(image):
    player_name = lst[idx + 1][2].replace(" ", "_")
    img_path = os.path.join(image_dir, f"{player_name}.png")
    
    if not os.path.exists(img_path):
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as handler:
            handler.write(img_data)
        print(idx+1, player_name, "Image downloaded")
    else:
        print(idx+1, player_name, "Image already exists")

print("Done")


