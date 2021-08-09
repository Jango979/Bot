from selenium import webdriver as wd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def parte1(DF):
    DIR_PATH = r'C:\WebDriver\chromedriver.exe'

    FirstURL = 'https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1628379602&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3dfb5d6e38-709c-0dc1-e1d7-3db40fbbdc54&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=0cac6de0ca674e6c93a782bad11a5b59'
    nameCSS_Selector = 'FirstName'
    surnameCSS_Selector = '//*[@id="LastName"]'
    usernameCSS_Selector = '#MemberName'
    passwordXPath_Selector = 'PasswordInput'
    countryId_Selector = 'Country'
    birthdayDayId_Selector = 'BirthDay'
    birthdayMonthId_Selector = 'BirthMonth'
    birthdayYearId_Selector = 'BirthYear'
    continuebutton1 = '#iSignupAction'



    for i in range(0,len(DF[0])):

        name, surname, password, Username, country, bd, bm, dy = DF.values[i][0], DF.values[i][1], DF.values[i][2],\
                                                                 DF.values[i][3], DF.values[i][4], str(DF.values[i][5]),\
                                                                 str(DF.values[i][6]), str(DF.values[i][7])
        driver = wd.Chrome(executable_path=DIR_PATH)
        driver.maximize_window()
        driver.get(FirstURL)

        driver.find_element_by_css_selector(usernameCSS_Selector).send_keys(Username)
        #WebDriverWait(driver,100)
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, continuebutton1)))
        driver.find_element_by_css_selector(continuebutton1).click()

        WebDriverWait(driver, 100)
        element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, passwordXPath_Selector)))
        element.send_keys(password)
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, continuebutton1)))
        button.click()

        time.sleep(2)
        button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, continuebutton1)))
        driver.find_element_by_name(nameCSS_Selector).send_keys(name)
        driver.find_element_by_xpath(surnameCSS_Selector).send_keys(surname)

        button.click()


        time.sleep(2)
        ListaPais = Select(driver.find_element_by_id(countryId_Selector))
        ListaPais.select_by_value(country)

        ListaDia = Select(driver.find_element_by_id(birthdayDayId_Selector))
        ListaDia.select_by_value(bd)

        ListaMes = Select(driver.find_element_by_id(birthdayMonthId_Selector))
        ListaMes.select_by_value(bm)

        driver.find_element_by_id(birthdayYearId_Selector).send_keys(dy)
        WebDriverWait(driver,2)
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, continuebutton1)))
        button.click()

        driver.quit()

