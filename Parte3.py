from selenium import webdriver as wd
import time
from pandas import read_csv
from Parte2 import NikeUser

class NikeBot():
    def __init__(self,name,password):
        self.password = str(password)
        self.username = str(name) + '@outlook.es'
        self.driver = wd.Chrome(executable_path=self.DIR_PATH)
        self.objectPage = 'https://www.nike.com/launch/t/air-jordan-1-low-travis-scott-fragment'
        self.LogIn_Selector = '#root > div > div > div.main-layout > div > header > div.d-sm-h.d-lg-b > section > div > ul > li.member-nav-item.d-sm-ib.va-sm-m > button'
        self.snkrspage = 'https://www.nike.com/mx/launch?s=upcoming'
        self.driver.maximize_window()
        self.VerifyCountry()
        self.LogIn()

    def LogIn(self):

        EmailTextArea = 'emailAddress'
        PassTextArea = 'password'

        self.driver.get(self.objectPage)
        self.driver.find_element_by_css_selector(self.LogIn_Selector).click()
        self.driver.find_element_by_name(EmailTextArea).send_keys(self.username+'@outlook.es')
        self.driver.find_element_by_name(PassTextArea).send_keys(self.password)
        self.driver.find_element_by_xpath("//input[@value='SIGN IN']").click()

    def VerifyCountry(self):
        ActualselectorCountry = '//*[@id="root"]/div/div/div[1]/div/header/div[1]/section/div/ul/li[4]/button/div/span'
        selectorCountry = 'locale-menu-item-language'
        CountryChange = '//*[@id="root"]/div/div/div[2]/div/div/div/div/div[2]/div/ul/li[73]/div/a/div/span[2]'

        self.driver.get(self.snkrspage)
        Actual_Country=self.driver.find_element_by_xpath(ActualselectorCountry).text
        if Actual_Country != 'United States':
            self.driver.find_element_by_xpath(ActualselectorCountry).click()
            self.driver.find_element_by_xpath(CountryChange).click()
        else:
            pass

    def Buy(self):
        Tallas = ['M 8 / W 9.5','M 8.5 / W 10','M 9 / W 10.5']
        for i in Tallas:
            try:
                self.driver.find_element_by_xpath("//*[contains(text(), '{}')]".format(i)).click()
                time.sleep(2)
                self.driver.find_element_by_xpath("//*[contains(text(), 'add to cart')]").click()
                time.sleep(2)
                self.driver.find_element_by_xpath("//*[contains(text(), 'Checkout')]").click()
            except:
                pass


DF = read_csv('BotList.csv',header=None)
ListOfBots=[]
for _ in range(0,len(DF[0])):
    password = str(DF.values[_][2])
    username = str(DF.values[_][3]) + '@outlook.es'
    nikeBot = NikeBot(username,password)
    ListOfBots.append(nikeBot)