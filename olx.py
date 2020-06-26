from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv
import parameters
from parsel import Selector
from selenium.webdriver.common.keys import Keys

writer = csv.writer(open("H://OLX.csv",'w',encoding="utf-8"))
writer.writerow(['name','location', 'url'])

driver=webdriver.Chrome('F:\\chromedriver')
driver.maximize_window()
sleep(2)
home=driver.get('https://www.olx.in/projects/maharashtra_g2001163/ready-to-move')
home=driver.current_url
print(home)
sleep(2)
try:
    while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5)
            next=driver.find_element_by_xpath('//*[@class="rui-3sH3b rui-23TLR rui-1zK8h"]').click()
                #next=driver.find_element_by_xpath('//button[contains(text(),'load more'])
            sleep(5)


except:
        print('No more pages to load.')
        sleep(5)
        for i in range(1,300):
            allLinks=driver.find_elements_by_xpath('//*[@class="_8HqL0"]//a')
            allLinks=[Link.get_attribute('href') for Link in allLinks]
            for Link in allLinks:
                driver.get(Link)
                sleep(5)
                sel = Selector(text=driver.page_source)
                name=sel.xpath('//h1//text()').extract()
                url=driver.current_url
                location=sel.xpath('//*[@class="_2wfvW"]//text()').extract()

                print(name)
                print(url)
                print(location)
                writer.writerow([name,url,location])


#driver.get(home)





#writer.writerow([name,url,location])
