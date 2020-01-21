#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:04:42 2020

@author: igreevaveronika
"""

from selenium import webdriver
import time
from math import log, sin

try:
    def calc(x):
        return str(log(abs(12*sin(int(x)))))
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
  
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    print(y)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    browser.execute_script("window.scrollBy(0, 100);")
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()