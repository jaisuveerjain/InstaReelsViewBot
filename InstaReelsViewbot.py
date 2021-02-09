
import time
from selenium import webdriver
for x in range (0,2):       # Replace for many times your video should be played|| Ex(0,100)-Video is played 100 times
    driver = webdriver.Chrome()
    driver.implicitly_wait(60)
    driver.maximize_window()

    driver.get("https://www.instagram.com/p/CJlKvUOjsuh/") #Replace with your instagram reels video URL
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/div/div/div[3]').click()
    time.sleep(12)   #Replace for what duration your video should be played
    driver.quit()
