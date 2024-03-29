from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.google.com/')

# find element "search field"
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait 4 sec
driver.implicitly_wait(4)

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify word what we search is on the text on the page, that means we opened right page
assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text

# verify the title matches to the expected
browser_title = driver.title
print(browser_title)
assert "Dress" in browser_title

# close browser
driver.quit()




