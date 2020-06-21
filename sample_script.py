from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='drivers/chromedriver')

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Lamp')

# wait 3 sec
driver.implicitly_wait(4)

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'Lamp' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'Lamp' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()