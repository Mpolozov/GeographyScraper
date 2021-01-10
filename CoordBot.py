from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def CoordBot(url):
    PATH = "/Users/mitchellpolozov/Downloads/chromedriver"
    driver = webdriver.Chrome(PATH)

    driver.get(url)

    search_bar = driver.find_element_by_name('q')
    search_bar.clear()

    time.sleep(5)

    search_bar.send_keys("Alabama")

    time.sleep(5)
    
    search_bar.send_keys(Keys.RETURN)

    time.sleep(10)

    driver.quit()

    #"https://www.geonames.org/search.html?q=New+York&country="

CoordBot("https://www.geonames.org/search.html?q=New+York&country=")