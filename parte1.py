from selenium import webdriver as wd
import Passworder as ps
from pandas import DataFrame

def FakeUser(numofbots):
    for _ in range(0, numofbots):
        _ = ps.Bot()
        _.Nombres()
        _.Password()
        _.Username()
        data = [_.nombreBot, _.apellidoBot, _.PSW, _.username]
        DF = DataFrame(data).T
        DF.to_csv('BotList.csv', mode='a', header=False,index=False)


DIR_PATH = r'C:\WebDriver\chromedriver.exe'
GmailUrlDir = '#gb > div > div:nth-child(1) > div > div:nth-child(1) > a'
googleURL = 'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fpc%3Dtopnav-about-n-en&flowName=GlifWebSignIn&flowEntry=SignUp'

driver = wd.Chrome(executable_path=DIR_PATH)
driver.maximize_window()
driver.get(googleURL)


