from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def Kdp_auto(email,password,description,booktitle,subtitle,firstname,lastname,keyword1,keyword2,keyword3,keyword4,keyword5,keyword6,keyword7,paperback,cover,Width,Height,price):
    ex = False

    try:
        driver = webdriver.Chrome(r"C:\Users\Ju_Eun\.wdm\drivers\chromedriver\win32\98.0.4758.102\chromedriver.exe")
    except:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    wait = WebDriverWait(driver, 10)
    longwait = WebDriverWait(driver, 120)
    superlongwait = WebDriverWait(driver,3600)

    driver.get("http://kdp.amazon.com")
    #driver.maximize_window()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signinButton"]/span/a')))
    driver.find_element(by=By.XPATH, value='//*[@id="signinButton"]/span/a').click()

    driver.find_element(by=By.XPATH, value='//*[@id="ap_email"]').send_keys(email)
    driver.find_element(by=By.XPATH, value='//*[@id="ap_password"]').send_keys(password + Keys.ENTER)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create-paperback-button"]/span/input')))
    driver.find_element(by=By.XPATH, value='//*[@id="create-paperback-button"]/span/input').click()

###################################### first page ###################################################################
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="data-print-book-title"]')))
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-title"]').send_keys(booktitle)
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-subtitle"]').send_keys(subtitle)
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-primary-author-first-name"]').send_keys(firstname)
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-primary-author-last-name"]').send_keys(lastname)

    driver.find_element(by=By.XPATH, value='//*[@id="non-public-domain"]').click()

    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-keywords-0"]').send_keys(keyword1)
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-keywords-1"]').send_keys(keyword2)
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-keywords-2"]').send_keys(keyword3)
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-keywords-3"]').send_keys(keyword4)
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-keywords-4"]').send_keys(keyword5)
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-keywords-5"]').send_keys(keyword6)
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-keywords-6"]').send_keys(keyword7)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cke_1_contents"]/iframe'))).click()
    driver.switch_to.frame(0)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body')))
    driver.find_element(by=By.XPATH, value='/html/body').send_keys(description)
    driver.switch_to.default_content()

    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-categories-button-proto-announce"]').click()

    ###################make a fucntion to choose shit fo you#######################
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Fiction')))
    driver.find_element(by=By.LINK_TEXT,value='Fiction').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkbox-fiction_general"]')))
    driver.find_element(by=By.XPATH, value='//*[@id="checkbox-fiction_general"]').click()
    ###################################################################################"
    driver.find_element(by=By.XPATH, value='//*[@id="category-chooser-ok-button"]/span/input').click()
    time.sleep(1)

    driver.find_element(by=By.XPATH,value='//*[@id="data-print-book-is-adult-content"]/div/div/fieldset/div[1]/div/label/input').click() # need keep click solution if not using sleep
    driver.find_element(by=By.XPATH, value='//*[@id="save-and-continue-announce"]').click()

#####################################second page###############################################################
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="free-print-isbn-btn-announce"]')))
    driver.find_element(by=By.XPATH, value='//*[@id="free-print-isbn-btn-announce"]').click()
    time.sleep(1) # i need to get rid of this somehow
    driver.find_element(by=By.XPATH, value='//*[@id="print-isbn-confirm-button-announce"]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="print-isbn-success-alert"]/div/div')))


    driver.find_element(by=By.XPATH, value='//*[@id="trim-size-btn-announce"]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="trim-size-standard-option-1-3-announce"]')))
    driver.find_element(by=By.XPATH, value='//*[@id="inputWidth"]').send_keys(Width)
    driver.find_element(by=By.XPATH,value='//*[@id="inputHeight"]').send_keys(Height)
    driver.find_element(by=By.XPATH, value='//*[@id="a-autoid-11"]/span/input').click()
    time.sleep(1) # i need to get rid of this as well

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="a-autoid-4-announce"]')))
    driver.find_element(by=By.XPATH, value='//*[@id="a-autoid-4-announce"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="a-autoid-7-announce"]').click()

    driver.find_element(by=By.XPATH,value='//*[@id="data-print-book-publisher-cover-choice-accordion"]/div[2]/div/div[1]/a/i').click()
    '''
    this code for try when fail clicking the cover choice button, deems unnecessary until extensive tests 
    while not ex:
        try:
            driver.find_element(by=By.XPATH,value='//*[@id="data-print-book-publisher-cover-choice-accordion"]/div[2]/div/div[1]/a/i').click()
            ex = True
        except:
            pass
    '''

    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="data-print-book-publisher-cover-file-upload-browse-button-announce"]')))
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-publisher-cover-file-upload-AjaxInput"]').send_keys(cover)
    longwait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="data-print-book-publisher-interior-file-upload-browse-button-announce"]')))
    driver.find_element(by=By.XPATH, value='//*[@id="data-print-book-publisher-interior-file-upload-AjaxInput"]').send_keys(paperback)
    longwait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="data-print-book-publisher-interior-file-upload-success"]/div')))


    longwait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="print-preview-noconfirm-announce"]')))
    driver.find_element(by=By.XPATH, value='//*[@id="print-preview-noconfirm-announce"]').click()

    longwait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="issues_by_severity"]/div[2]/h2')))
    superlongwait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="printpreview_approve_button_enabled"]')))
    driver.find_element(by=By.XPATH, value='//*[@id="printpreview_approve_button_enabled"]').click()

    longwait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="save-and-continue-announce"]')))
    driver.find_element(by=By.XPATH, value='//*[@id="save-and-continue-announce"]').click()

########################################## third page ##############################################################
    longwait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="data-pricing-print-us-price-input"]/input')))
    driver.find_element(by=By.XPATH, value='//*[@id="data-pricing-print-us-price-input"]/input').send_keys(price)

    longwait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="data-pricing-print"]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/span/div')))
    driver.find_element(by=By.XPATH, value='//*[@id="data-pricing-print"]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/span/div').click()

    longwait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="save-and-publish-announce"]')))
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="data-pricing-print"]/div/div/div[7]/div/div[1]/div/div/div[1]/div/div[4]/div/div/div/div/div/div/span')))
    driver.find_element(by=By.XPATH, value='//*[@id="save-and-publish-announce"]').click()
    time.sleep(10)