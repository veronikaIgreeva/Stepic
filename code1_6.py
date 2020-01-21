from selenium import webdriver
import time


try:
    link = "hhttp://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_css_selector(".first_block .first")
    name.send_keys("Ivan")

    surname = browser.find_element_by_css_selector(".first_block .second")
    surname.send_keys("Ivanov")

    email = browser.find_element_by_css_selector(".first_block .third")
    email.send_keys("ivan@ivanov.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

