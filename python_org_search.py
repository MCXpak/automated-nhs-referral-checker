from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

details = []
f = open("C:\\Users\moura\Desktop\Projects\Programming\info\details.txt", "r")
for x in f:
    details.append(x.replace("\n",""))

driver = webdriver.Chrome('./chrome-driver/chromedriver.exe')
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

assert "No results found." not in driver.page_source
