#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:42:13 2020

@author: igreevaveronika
"""

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    button = browser.find_element_by_id("button")
    button.click()
           
finally:
    browser.quit()
    
    

