from selenium import webdriver
import time

driver = webdriver.Chrome()  

def scroll_control(scroll_count):
    for i in range(scroll_count):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1) 
