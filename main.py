from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


def start_chrome():
    print('Starting...')
    global driver
    try:
        driver = webdriver.Chrome()
        driver.get('http://sama.ssu.ac.ir/')
    except:
        print('The browser is not supported :(')

def start_firefox():
    print('Starting...')
    global driver
    try:
        driver = webdriver.Firefox()
        driver.get('http://sama.ssu.ac.ir/')
    except:
        print('The browser is not supported :(')

def survey():
    try:
        frame = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_frLoadAsp')
        driver.switch_to.frame(frame)
    except:
        pass
    i = 4
    OPTION = input('Which option? 1 to 6\n')
    while i<=38:
        xpath = '/html/body/center/form/table[' + str(i) + ']/tbody/tr/td['+ OPTION +']/input'
        driver.find_element(By.XPATH, xpath).click()
        i += 2
    print('Done and dusted (; \n')

browser = input('(C)hrome or (F)irefox?\n')
if browser.lower() == 'c':
    start_chrome()
elif browser.lower() == 'f':
    start_firefox()
else:
    print('Browser not found :(')

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.ID, 'UserCode')))
while True:
    app = input('(S)tart or (Q)uit?\n')
    if app.lower() == 's':
        survey()
    elif app.lower() == 'q':
        break
    else:
        print("We can either (S)tart or (Q)uit, there's no middle ground! \n")