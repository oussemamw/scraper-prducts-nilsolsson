from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import csv

driver = webdriver.Chrome()
driver1 = webdriver.Chrome()

driver.get('https://nilsolsson.se/sv/Produkter')
table_info = ['title', 'price', 'description', 'image', 'sub_categ', 'categ']


csv_data=[]
def crawl(d):
    data={}
    product_links=d.find_elements_by_class_name("itemnamelink")
    for product in product_links:
        link=product.get_attribute("href")
        driver1.get(link)
        data['title']=driver1.find_element_by_class_name('title').text
        data['price']=driver1.find_element_by_class_name('price').text
        data['description']=driver1.find_element_by_class_name('description').text
        data['image']=driver1.find_element_by_class_name('image_links').get_attribute("href")
        list_categ=driver1.find_elements_by_class_name('breadlink')
        if len(list_categ)>3:
            data['sub_categ']=list_categ[-1].text
            data['categ']=list_categ[-2].text
        else:
            data['sub_categ']=""
            data['categ']=list_categ[-1].text
        csv_data.append(data)
        data={}
    
link_categ=[]
all_categ=driver.find_elements_by_class_name("group-link")
for categ in all_categ:
    link_categ.append(categ.get_attribute("href"))


for l in link_categ:
    driver.get(l)
    link_sub_categ=[]
    try:
        all_sub_categ=driver.find_elements_by_class_name("group-link")
        for sub_categ in all_sub_categ:
            link_sub_categ.append(sub_categ.get_attribute("href"))

        

    except:
        pass
    if link_sub_categ:

        for sub_l in link_sub_categ:

            driver.get(sub_l)
            crawl(driver)



    else:
        crawl(driver)

with open('data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = table_info)
        writer.writeheader()
        writer.writerows(csv_data)

        


