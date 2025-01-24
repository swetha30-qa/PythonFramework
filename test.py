import time
from selenium import webdriver
opts = webdriver.EdgeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Edge(options=opts)
driver.get('https://www.playstation.com/en-sg/')
time.sleep(4)