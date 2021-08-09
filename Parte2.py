from selenium import webdriver as wd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

DIR_PATH = r'C:\WebDriver\chromedriver.exe'
snkrspage = 'https://www.nike.com/mx/launch?s=upcoming'

selectorCountry = 'locale-menu-item-language'
ActualselectorCountry = '//*[@id="root"]/div/div/div[1]/div/header/div[1]/section/div/ul/li[4]/button/div/span'
CountryChange = '//*[@id="root"]/div/div/div[2]/div/div/div/div/div[2]/div/ul/li[73]/div/a/div/span[2]'
LogIn_Selector = '#root > div > div > div.main-layout > div > header > div.d-sm-h.d-lg-b > section > div > ul > li.member-nav-item.d-sm-ib.va-sm-m > button'

objectPage = 'https://www.nike.com/launch/t/air-jordan-1-low-travis-scott-fragment'


driver = wd.Chrome(executable_path=DIR_PATH)
driver.maximize_window()
def VerifyCountry():
    driver.get(snkrspage)
    Actual_Country=driver.find_element_by_xpath(ActualselectorCountry).text
    if Actual_Country != 'United States':
        driver.find_element_by_xpath(ActualselectorCountry).click()
        driver.find_element_by_xpath(CountryChange).click()



def LogIn():
    EmailTextArea = 'emailAddress'
    PassTextArea = 'password'
    LogIn_Input = '//*[@id="3e3d3ade-7bf3-40d2-8cf2-a67120e15015"]'

    driver.get(objectPage)
    driver.find_element_by_css_selector(LogIn_Selector).click()
    driver.find_element_by_name(EmailTextArea).send_keys('Tacos')
    driver.find_element_by_name(PassTextArea).send_keys('1')
    #driver.find_element_by_xpath(LogIn_Input).click()

def JoinUs():
    JoinUs_id = '//*[@id="bb438342-71ab-4ab8-8232-ab9a3c0cb533"]'
    Email_xpath = '//*[@id="86641a66-4732-4a10-897d-5cf295d9f922"]'
    Pass_xpath = '//*[@id="52e96ba6-a694-4e07-8518-878fbf5aaed4"]'
    FName_xpath = '//*[@id="83345800-104e-4db2-9240-3840eb7eda6f"]'
    LName_xpath = '//*[@id="50911e98-e8d5-4535-8a14-69a89cc4ae22"]'
    Birth_xpath = '//*[@id="1fcc08c0-c9c5-47e6-9c35-09155c18ab1c"]'
    #driver.fin
    time.sleep(10)
    driver.find_element_by_css_selector(LogIn_Selector).click()
    time.sleep(10)
    SessionId=driver.find_element_by_xpath("//*[contains(text(), 'Join Us.')]").parent.session_id
    print(SessionId)
    print('//*[@id="{}"]'.format(SessionId))
    driver.find_element_by_xpath("//*[contains(text(), 'Join Us.')]").click()
    driver.find_element_by_name('emailAddress').send_keys('Tacos1@asd.cx')
    driver.find_element_by_name('password').send_keys('Tacos222222')
    driver.find_element_by_name('firstName').send_keys('Juan ban')
    driver.find_element_by_name('lastName').send_keys('SANCHO')
    driver.find_element_by_name('dateOfBirth').send_keys('data-ddlabel','12071992')
    #driver.find_element_by_xpath("//*[contains(text(), 'Male')]").click()
    driver.find_elements_by_tag_name('li')[12].click()
    driver.find_element_by_name('receiveEmail').click()
    driver.find_element_by_xpath("//input[@value='JOIN US']").click()
    while True:
        try:
            driver.find_element_by_xpath("//input[@value='Dismiss this error']").click()
            print('Fail on sign in retry in 10s')
            time.wait(10)
            driver.find_element_by_xpath("//input[@value='JOIN US']").click()
        except:
            break

VerifyCountry()
#LogIn()
JoinUs()


