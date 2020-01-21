#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:33:59 2020

@author: igreevaveronika
"""

from selenium import webdriver
import time
from math import log, sin


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    def calc(x):
        return str(log(abs(12*sin(int(x)))))
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    print(y)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
        
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
       
finally:
    time.sleep(10)
    browser.quit()