# coding: utf-8

# Mission to Mars



#Install Modules
#!pip install splinter
#!pip install --user splinter
#!pip install Ipython




#Import Dependencies
from bs4 import BeautifulSoup 
from splinter import Browser
#////from Ipython.display import Image
from selenium import webdriver
import pandas as pd
import time
import shutil
import requests




#https://splinter.readthedocs.io/en/latest/drivers/chrome.html
#!which chromedriver
# Create list
mars_list ={}
#Browser Initialization
def browser_init():

    #Executable Driver Path
    executable_path={'executable_path':'/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)
def scrape():

# --- NASA Mars News

    try:
        browser=browser_init()
        #URL page visit
        url = "https://mars.nasa.gov/news"
        browser.visit(url)


        #HTML n Soup Object
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')

        #Find text
        news_title = soup.find("div", class_='content_title').text
        news_p = soup.find("div", class_= 'rollover_description_inner').text
        #Dictionary addition
        mars_list["news_title"] = news_title
        mars_list["news_paragraph"]= news_p
        return mars_list
    finally:
        browser.quit()

  

#---JPL Mars Space Images - Featured Image

    try:
        browser=browser_init()


#Website access
        main_img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(main_img_url)

#HTML n Soup Object
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')

#Specified path scraping
        img_url = soup.find('div', class_='fancybox-inner fancybox-skin fancybox-dark-skin fancybox-dark-skin-open')['src']

#Featured Image full url link connecting
        feat_img_url="https://www.jpl.nasa.gov" + img_url
#Display full url link
        feat_img_url
#Dictinary addition
        mars_list["Featured Image"] = feat_img_url
        return mars_list
    finally:
        browser.quit()

#Request to download and save and display an image
#img_data = requests.get(feat_img_url).content
#with open('PIA16694_ip.jpg', 'wb') as handler:
 #   handler.write(img_data)

#////img = Image.open('PIA16694_ip.jpg')
#////img.show()


#----Mars Weather

    try:
        browser=browser_init()

#Website access
        main_wthr_url="https://twitter.com/marswxreport?lang=en"
        browser.visit(main_wthr_url)

#HTML n Soup Object
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')

#Find text
        mars_weather=soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
#Display output
        mars_weather
#Dictinary addition
        mars_list["Latest Mars Weather"] = mars_weather
        return mars_list
    finally:
        browser.quit()


#--- Mars Facts

    try:
        browser=browser_init()



#Website access
        main_facts_url="https://space-facts.com/mars/"
        browser.visit(main_facts_url)




#HTML n Soup Object
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')




#Find and create a Dataframe table and convert to Html string
        facts_tbl = soup.table.find_all('table', id="tablepress-mars", class_="tablepress tablepress-id-mars")
        column1= facts_tbl.find_all('td', class_='column-1')
        column2= facts_tbl.find_all('td', class_='column-2')

        measurements=[]
        units=[]

        for x in column1:
            measure= x.text.strip()
            measurements.append(measure)

        for x in column2:
            unit= x.text.strip()
            units.append(unit)  
        facts_df=pd.DataFrame({"Measuments": measurements,
                      "Units": units})
          
#Convert extracted table to Html string
        fact_tbl_html=facts_df.to_html(header=False, index=False)
        fact_tbl_html
#Dictinary addition
        mars_list["Mars Facts"] = fact_tbl_html
        return mars_list
    finally:
        browser.quit()


# Mars Hemispheres

    try:
        browser=browser_init()


#Website access
        hemi_url = 'https://astrogeology.usgs.gov/maps/mars-viking-hemisphere-point-perspectives/'

        browser.visit(hemi_url)



#HTML n Soup Object
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        hemi = soup.find_all('div', class_='decription')



#Main Website Access
        main_img_url= 'https://astrogeology.usgs.gov/search/map/Mars/Viking/'




#Create a list
        hemi_img_url=[]
        
#Loop through list items and create a dictionary
        for x in hemi:
            title=x.find('h3').text
            title_end_url=str(title)
    #Hemisphere Title string lower case and join with underscore to get a working webpage
            title_end_url.lower()
            '_'.join(title_end_url)
            joined_img_url=main_img_url+title_end_url
            browser.visit(joined_img_url)
            joined_img_url=browser.html
            soup_1 = BeautifulSoup(joined_img_url, 'html.parser')
            img_url = joined_img_url + soup_1.find('img', class_='wide-image')['src']
    
    #Save image url and title
            #img_data = requests.get('title','img_url').content
            #with open('img', 'wb') as handler:
            #handler.write(img_data)

    
    #Append the dictionary and print output
            hemi_img_url.append({"title": title, "img_url" : img_url })
            mars_list["Mars Hemispheres"]=hemi_img_url
            return mars_list
    finally:
        browser.quit()

    
    
    

