from selenium import webdriver as wd
import time
from pandas import read_csv



class NikeUser():
    def __init__(self,DF):
        self.DIR_PATH = r'C:\WebDriver\chromedriver.exe'
        self.snkrspage = 'https://www.nike.com/mx/launch?s=upcoming'

        self.CountryChange = '//*[@id="root"]/div/div/div[2]/div/div/div/div/div[2]/div/ul/li[73]/div/a/div/span[2]'
        self.LogIn_Selector = '#root > div > div > div.main-layout > div > header > div.d-sm-h.d-lg-b > section > div > ul > li.member-nav-item.d-sm-ib.va-sm-m > button'

        self.objectPage = 'https://www.nike.com/launch/t/air-jordan-1-low-travis-scott-fragment'

        self.driver = wd.Chrome(executable_path=self.DIR_PATH)
        self.driver.maximize_window()

        self.DF = DF

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



    def LogIn(self):
        for _ in range(0,len(self.DF[0])):
            self.username = str(DF.values[_][3])
            self.password = str(DF.values[_][2])


            EmailTextArea = 'emailAddress'
            PassTextArea = 'password'

            self.driver.get(self.objectPage)
            self.driver.find_element_by_css_selector(self.LogIn_Selector).click()
            self.driver.find_element_by_name(EmailTextArea).send_keys(self.username+'@outlook.es')
            self.driver.find_element_by_name(PassTextArea).send_keys(self.password)
            self.driver.find_element_by_xpath("//input[@value='SIGN IN']").click()

    def JoinUs(self):


        for _ in range(0,len(self.DF[0])):
            self.fname = str(DF.values[_][0])
            self.lname = str(DF.values[_][1])
            self.password = str(DF.values[_][2])
            self.username = str(DF.values[_][3])+'@outlook.es'
            self.bithday = str(DF.values[_][5])+str(DF.values[_][6])+str(DF.values[_][7])

            while True:
                self.driver.get(self.objectPage)
                time.sleep(2)
                self.driver.find_element_by_css_selector(self.LogIn_Selector).click()
                time.sleep(2)
                SessionId = self.driver.find_element_by_xpath("//*[contains(text(), 'Join Us.')]").parent.session_id
                print(SessionId)
                print('//*[@id="{}"]'.format(SessionId))
                self.driver.find_element_by_xpath("//*[contains(text(), 'Join Us.')]").click()
                self.driver.find_element_by_name('emailAddress').send_keys(self.username)
                self.driver.find_element_by_name('password').send_keys(self.password)
                self.driver.find_element_by_name('firstName').send_keys(self.fname)
                self.driver.find_element_by_name('lastName').send_keys(self.lname)
                self.driver.find_element_by_name('dateOfBirth').send_keys('data-ddlabel',self.bithday)
                #driver.find_element_by_xpath("//*[contains(text(), 'Male')]").click()
                self.driver.find_elements_by_tag_name('li')[12].click()
                #self.driver.find_element_by_name('receiveEmail').click()
                self.driver.find_element_by_xpath("//input[@value='JOIN US']").click()

                try:
                    time.sleep(3)
                    self.driver.find_element_by_xpath("//input[@value='Dismiss this error']").click()
                    print('Fail on sign in retry in 10s')
                    time.sleep(10)
                    self.driver.find_element_by_xpath("//input[@value='JOIN US']").click()

                except:
                    print('Objetivo inscrito')
                    time.sleep(4)
                    self.driver.quit()
                    self.driver = wd.Chrome(executable_path=self.DIR_PATH)
                    self.driver.maximize_window()
                    self.driver.get(self.objectPage)
                    break
                else:
                    continue






DF = read_csv('BotList.csv',header=None)
NkUser = NikeUser(DF)
NkUser.VerifyCountry()
NkUser.JoinUs()