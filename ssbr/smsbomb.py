from selenium import webdriver
import time

def snap(driver):
    driver.get('https://app.snapp.taxi/login/?redirect_to=%2Fpre-ride%3Futm_source%3Dwebsite%26utm_medium%3Dwebapp-button')
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="login-input"]').click()
    driver.find_element_by_xpath('//*[@id="login-input"]').send_keys('09391662579')
    driver.find_element_by_xpath('//*[@id="next-button"]').click()
    
def alopek(driver):
    driver.get('https://app.alopeyk.com/login')
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="login-input"]').send_keys('09391662579')
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div/div/div/div[2]/div/div/div[2]/form/div[2]/button').click()

def tapsi(driver):
    driver.get('https://app.tapsi.cab/')
    driver.refresh()
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="exampleField"]').send_keys('09391662579')
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]').click()

def rubika(driver):
    driver.get('https://web.rubika.ir/')
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="login"]/div[2]/form/div[2]/div[2]/div[1]/div[2]/input').send_keys('9391662579')
    driver.find_element_by_xpath('//*[@id="login"]/div[2]/form/div[2]/div[2]/div[3]/button').click()

driver = webdriver.Firefox()
for x in range(20):
    snap(driver)
    rubika(driver)
    tapsi(driver)
    alopek(driver)