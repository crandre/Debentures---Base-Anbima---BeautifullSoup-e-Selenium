from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pandas as pd
import time

option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path= 'C:\webdrivers\geckodriver')

url = "https://data.anbima.com.br/debentures"
driver.get(url)

time.sleep(3)

firstclick = driver.find_element_by_xpath("/html/body/div[1]/div/main/main/div/div[2]/div[1]/div/div/label").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pagination"]/div[1]/div/div/ul/li[4]/div'))).click()

time.sleep(5)

driver.find_element_by_class_name('container')
ai = driver.find_element_by_class_name('container')

b1 = ai.find_elements_by_class_name('debentures-list-item')
total_list = []
lista_ind_deb = []

for tudo2 in range(3):
    tudo1 = str(tudo2)
    time.sleep(3)
    mySelectElement = driver.find_element_by_id('debentures-item-nome-fundo-'+tudo1+'').click()
    c11 = driver.find_element_by_xpath('/html/body/div[1]/div/header/div[2]/div/h1') 
    driver.find_element_by_class_name('page--particulars')
    aii = driver.find_element_by_class_name('page--particulars')
    b11 = aii.find_elements_by_tag_name('div')
    
    lista_ind_deb.append(c11.text)
    for tudo_deb in b11:
        lista_ind_deb.append(tudo_deb.text)
        
    #print(lista_ind_deb)


    WebDriverWait(driver, 10000000000000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-nav-debentures"]'))).click()
            
print(lista_ind_deb)
final = []
for i in range(len(lista_ind_deb)):
    final.append(lista_ind_deb[i].split("u'"))
    

df_final = pd.DataFrame(final)
df_final.to_csv('planilhainfoindivTESTE.csv', encoding='utf-16')
