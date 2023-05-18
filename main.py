from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import schedule
from dotenv import load_dotenv
from time import sleep
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import pyautogui

load_dotenv()

"""
    monday 20:40 => türk dili
    wednesday 21:35 => kariyer planlama
    thursday 21:00 => tarih
    friday 14:00 => makineye giriş
"""

options = Options()
options.add_argument("start-maximized")
PATH = "/Users/user/local/bin/chromedriver"
driver = webdriver.Chrome(PATH, options=options)
URL = "https://online.deu.edu.tr/portal"

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


# Links to online classes and function to open that screen
today = datetime.today()
formatted_date = new_date = str(today.day) + "." + str(today.month) + "." + str(today.year)

class Classes:

    def __init__(self):
        self.turk_dili_live = "https://online.deu.edu.tr/portal/site/a70bb352-74f5-460f-9aa1-53db71291272/tool/8c8fc6c3-16dc-436f-8af6-6db448ccc3bf"
        self.kariyer_live = "https://online.deu.edu.tr/portal/site/fd0b035f-ffe8-4825-86dc-9b0c91429648/tool/9c0f0c62-095f-4256-8a5b-c9b824fa9334"
        self.tarih_live = "https://online.deu.edu.tr/portal/site/e0947124-b787-4f19-b08b-80595d624c29/tool/25969e6a-0f91-4540-8de6-65eb7c334b6a"
        self.makine_live = "https://online.deu.edu.tr/portal/site/8c779814-492e-4743-9197-40099611c38f/tool/b574c72c-f901-4a50-a036-f7aa7cecdc18"


    def initalizer(self):
        driver.get(URL)
        print("Process started..")

        # Login info passed 
        login_element = driver.find_element("id", "eid")
        password_element = driver.find_element("id", "pw")
        submit_btn = driver.find_element("id", "submit")


        login_element.send_keys(username)
        password_element.send_keys(password)
        submit_btn.click()
        sleep(2)
        pos_x, pos_y = 720, 427
        pyautogui.moveTo(pos_x, pos_y, duration=2, tween=pyautogui.easeInOutQuad)


    def monday_class(self):
        self.initalizer()
        driver.get(self.turk_dili_live)
        print("Accessed live menu..")
        sleep(10)

        start_date_table = driver.find_elements(By.CLASS_NAME, "sorting_1")
        counter = 1

        for d in start_date_table:
            date_text = d.text
            
            if len(date_text.strip()) > 0:
                format_date = date_text.split()[0]
                if formatted_date == format_date:
                    # Get the link to live lesson
                    get_link_xpath = driver.find_element(By.XPATH, f'//*[@id="bbb_meeting_table"]/tbody/tr[{counter}]/td[1]/a').click()
                    print("Found the link..")
                    sleep(10)
                    
                    join_link = driver.find_element(By.ID, "joinMeetingLink").click()
                    print("Clicked link..")
                    sleep(150)
                    pyautogui.click()
                    print("Process finished")
    
            counter += 1 
        

    def wednesday_class(self):
        self.initalizer()
        driver.get(self.kariyer_live)
        print("Accessed live menu..")
        sleep(10)

        start_date_table = driver.find_elements(By.CLASS_NAME, "sorting_1")
        counter = 1

        for d in start_date_table:
            date_text = d.text
            
            if len(date_text.strip()) > 0:
                format_date = date_text.split()[0]
                if formatted_date == format_date:
                    # Get the link to live lesson
                    get_link_xpath = driver.find_element(By.XPATH, f'//*[@id="bbb_meeting_table"]/tbody/tr[{counter}]/td[1]/a').click()
                    print("Found the link..")
                    sleep(10)
                    
                    join_link = driver.find_element(By.ID, "joinMeetingLink").click()
                    print("Clicked link..")
                    sleep(150)
                    pyautogui.click()
                    print("Process finished")
    
            counter += 1 


    def thursday_class(self):
        self.initalizer()
        driver.get(self.tarih_live)
        print("Accessed live menu..")
        sleep(10)

        start_date_table = driver.find_elements(By.CLASS_NAME, "sorting_1")
        counter = 1

        for d in start_date_table:
            date_text = d.text
            
            if len(date_text.strip()) > 0:
                format_date = date_text.split()[0]
                if formatted_date == format_date:
                    # Get the link to live lesson
                    get_link_xpath = driver.find_element(By.XPATH, f'//*[@id="bbb_meeting_table"]/tbody/tr[{counter}]/td[1]/a').click()
                    print("Found the link..")
                    sleep(10)
                    
                    join_link = driver.find_element(By.ID, "joinMeetingLink").click()
                    print("Clicked link..")
                    sleep(150)
                    pyautogui.click()
                    print("Process finished")
    
            counter += 1 


    def friday_class(self):
        self.initalizer()
        driver.get(self.makine_live)
        print("Accessed live menu..")
        sleep(10)

        start_date_table = driver.find_elements(By.CLASS_NAME, "sorting_1")
        counter = 1

        for d in start_date_table:
            date_text = d.text
            
            if len(date_text.strip()) > 0:
                format_date = date_text.split()[0]
                if formatted_date == format_date:
                    # Get the link to live lesson
                    get_link_xpath = driver.find_element(By.XPATH, f'//*[@id="bbb_meeting_table"]/tbody/tr[{counter}]/td[1]/a').click()
                    print("Found the link..")
                    sleep(10)
                    
                    join_link = driver.find_element(By.ID, "joinMeetingLink").click()
                    print("Clicked link..")
                    sleep(150)
                    pyautogui.click()
                    print("Process finished")
    
            counter += 1 


# Schedule functions to make them work every weeek
cls = Classes()
schedule.every().monday.at("20:45").do(cls.monday_class)
schedule.every().wednesday.at("21:40").do(cls.wednesday_class)
schedule.every().thursday.at("21:05").do(cls.thursday_class)
schedule.every().friday.at("14:05").do(cls.friday_class)


# Function to run script everytime 
while True:
    schedule.run_pending()
    time.sleep(1)




