import os
from selenium import webdriver
from twilio.rest import Client
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_argument("--headless")

sid_token = []
f = open("C:\\Users\moura\Desktop\Projects\Programming\info\sid_token.txt", "r")
for x in f:
    sid_token.append(x.replace("\n",""))

print(sid_token)
account_sid = sid_token[0]
auth_token = sid_token[1]
client = Client(account_sid, auth_token)

'''
Details text file must contain:

Refernce Number
Year of Birth
Access Code

in this order, each in one line. 

If you'd like, you can add the datils straight to the corresponding variable e.g. yearOfBirth.send_keys("1990");
'''
details = []
f = open("C:\\Users\moura\Desktop\Projects\Programming\info\details.txt", "r")
for x in f:
    details.append(x.replace("\n",""))

driver = webdriver.Chrome('./chrome-driver/chromedriver.exe', options=chrome_options)
driver.get("https://refer.nhs.uk/login")
wait = WebDriverWait(driver, 20)

wait.until(EC.visibility_of_element_located((By.ID, 'ubrn')))
refNumber = driver.find_element(by=By.ID, value="ubrn")
yearOfBirth = driver.find_element(by=By.NAME, value="input-birthYear")
accessCode = driver.find_element(by=By.NAME, value="input-loginPassword")
refNumber.send_keys(details[0])
refNumber.send_keys(Keys.TAB)
yearOfBirth.send_keys(details[1])
yearOfBirth.send_keys(Keys.TAB)
accessCode.send_keys(details[2])
accessCode.send_keys(Keys.ENTER)
wait.until(EC.visibility_of_element_located((By.NAME, 'lnk-change-appointment')))
changeDateAndTime = driver.find_element(by=By.NAME, value="lnk-change-appointment")
changeDateAndTime.click()
wait.until(EC.visibility_of_element_located((By.NAME, 'msg-no-appointment')))
appointmentStatus = driver.find_element(by=By.NAME, value="msg-no-appointment")
print(appointmentStatus.text)

message = client.messages \
    .create(
         body=appointmentStatus.text,
         from_='+14302161764',
         to='+447921518188'
     )

assert "No results found." not in driver.page_source
driver.quit()
