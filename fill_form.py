import pandas as pd
from selenium import webdriver
import time
from variables import *


web=webdriver.Chrome("./chromedriver.exe")

participants=pd.read_excel("./participants.xlsx")
for index, row in participants.iterrows():
    participant_name=row['Name']
    participant_reg_no=row['Reg. No']

    web.get('https://docs.google.com/forms/d/e/1FAIpQLSckKFDYqXQ9MeN-1YkfwiHEUgswCnpwCggOixFDX38cUxrCSA/viewform')
    time.sleep(0.5)

    form_email=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    form_email.send_keys(club_email)

    club_or_chapter_dropdown=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    club_or_chapter_dropdown.click()
    time.sleep(0.2)
    club_or_chapter_option = web.find_elements_by_xpath("//div//span[contains(., 'Club')]")
    for i in club_or_chapter_option:
        try:
            i.click()
        except Exception as e:
            print(e)

    club_or_chapter_name_dropdown=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    club_or_chapter_name_dropdown.click()
    time.sleep(0.2)
    club_or_chapter_name_option = web.find_elements_by_xpath("//div//span[contains(., 'Dance club')]")
    for i in club_or_chapter_name_option:
        try:
            i.click()
        except Exception as e:
            print(e)
    time.sleep(0.2)

    page_one_submit=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    page_one_submit.click()
    time.sleep(0.2)

    form_event_name=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_event_name.send_keys(event_name)

    form_event_date=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    form_event_date.send_keys(event_date)

    page_two_submit=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    page_two_submit.click()
    time.sleep(0.2)

    form_participant_name=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_participant_name.send_keys(participant_name)

    form_participant_registration_number=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_participant_registration_number.send_keys(participant_reg_no)

    final_submit_button=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span')
    final_submit_button.click()
    time.sleep(0.2)

    submit_message=web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
    if(submit_message.text=="Your response has been recorded."):
        print("Attendance marked for", participant_name)