from selenium import webdriver

browser = webdriver.Firefox(executable_path='/home/omah/TDD/geckodriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
