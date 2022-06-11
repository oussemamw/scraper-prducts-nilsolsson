from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome()
driver1 = webdriver.Chrome()

driver.get('https://nilsolsson.se/sv/Produkter')



def crawl(d):
    product_links=d.find_elements_by_class_name("itemnamelink")
    for product in product_links:
        link=product.get_attribute("href")
        driver1.get(link)


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

        print(link_sub_categ)

    except:
        pass
    if link_sub_categ:

        for sub_l in link_sub_categ:

            driver.get(sub_l)
            crawl(driver)



    else:
        crawl(driver)

        


