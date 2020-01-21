#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:29:44 2020

@author: igreevaveronika
"""

import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
#element.send_keys(file_path)
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

