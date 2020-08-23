from selenium import webdriver

browser = webdriver.Chrome('./chromedriver') 
browser.get('http://localhost:8000')

print("------------------------")
print(browser.title)
print("------------------------")
assert 'Django' in browser.title

#browser.quit()