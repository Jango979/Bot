from selenium import webdriver as wd

def FakeUser():

    pass


DIR_PATH = r'C:\WebDriver\chromedriver.exe'
GmailUrlDir = '#gb > div > div:nth-child(1) > div > div:nth-child(1) > a'
googleURL = 'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fpc%3Dtopnav-about-n-en&flowName=GlifWebSignIn&flowEntry=SignUp'

driver = wd.Chrome(executable_path=DIR_PATH)
driver.maximize_window()
driver.get(googleURL)


