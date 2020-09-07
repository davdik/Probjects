from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\1\\chromedriver.exe")
driver.get('https://translate.google.com/')
print(driver.current_url)
print(driver.title)
driver.find_elemnt_by_id("source").click()
driver.find_elemnt_by_id("source").send_keys("hello")


driver.quit()