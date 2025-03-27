# create the project : scrapy startproject genshinCharacters
# move this file into "scrapyGenshinCharacters\scrapyGenshinCharacters\spiders"
# launch : scrapy crawl genshinCharacters
import scrapy
import os
import requests
import csv


class MySpider(scrapy.Spider):
    name = "genshinCharacters"
    start_urls = [
    "https://www.genshin-impact.fr/personnages/",
    ]

    def parse(self, response):
        with open('genshin_characters.csv', mode='w', newline='', encoding='utf-16') as file:
            writer = csv.writer(file)
            writer.writerow(["Nom", "Rarete", "Arme", "Element", "Base ATQ", "Base DEF", "Base PV", "Lien"])
        # The logic of web scraping is defined here
        chararcters = response.css(".et_pb_toggle_content.clearfix")
        for chararcterLink in chararcters.css('a::attr(href)').getall():
            link = chararcterLink
            yield response.follow(link, self.parse_character)


    def parse_character(self, response):
        name = response.url.split('/')[-2].capitalize()
        tableStats = response.css('.row-hover')
        stats = []
        for stat in tableStats.css('tr')[1:4]:
            stats = stats + stat.css('td::text').getall()
        baseATQ = stats[2]
        baseDEF = stats[5]
        basePV = stats[8]
 
        build = response.css(".block_centered").css('img::attr(data-src)').get()
        
        type = response.css("h2::text").get()
        if not type:
            type = ''.join(response.css(".wdg-select-all-ok::text").getall())

        rarete = type.split(" ")[0]
        arme = ' '.join(type.split("/")[0].split(" ")[1:])
        element = type.split("/")[1]

        directory = 'BuildGenshinCharacters'
        if not os.path.exists(directory):
            os.makedirs(directory)

        if build:
            image_name = os.path.join(directory, f"{name}.png")
            if not os.path.exists(image_name):
                img_data = requests.get(build).content
                with open(image_name, 'wb') as handler:
                    handler.write(img_data)

        with open('genshin_characters.csv', mode='a', newline='', encoding='utf-16') as file:
            writer = csv.writer(file)
            writer.writerow([name, rarete, arme, element, baseATQ, baseDEF, basePV, response.url])

