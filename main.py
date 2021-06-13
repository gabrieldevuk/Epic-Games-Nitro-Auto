from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
with open("emails.txt") as f:
    for line in f:
        email = line.strip("\n")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
        driver.get("https://www.epicgames.com/store/en-US/p/discord--discord-nitro")
        sleep(4)
        driver.find_element_by_xpath('//*[@id="user"]/ul/li/a/span').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="to-register"]/span').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="login-with-epic"]').click()
        name = random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz")
        lastname = random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz")
        displayname = random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz")
        password = "1" + "!" + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz")
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[2]/div[1]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[2]/div[1]/div/input').send_keys(name)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[2]/div[2]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[2]/div[2]/div/input').send_keys(lastname)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[3]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[3]/div/input').send_keys(displayname)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[4]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[4]/div/input').send_keys(email)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[5]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[5]/div/input').send_keys(password)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/label[2]/span[1]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[7]').click()
        input(f"Prompted Captcha to solve, please solve this manually! Press enter when done!")
        print(f"Account created with email: {email} and password: {password}")
        input("Awaiting verification code, check email and enter code manually.")
        driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/main/div/div[3]/div/div/div[2]/div[2]/div/aside/div/div/div[4]/div/button/span').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="agree"]').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div/div[2]/button').click()
        sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[4]/div[1]/div[2]/div[4]/div/div/label/div[1]/span').click
        driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[4]/div[1]/div[2]/div[5]/div/div/button').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[4]/div[1]/div[2]/div[6]/div[2]/div/div[2]/button[2]').click()
