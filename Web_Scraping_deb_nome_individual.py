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

mySelectElement = driver.find_element_by_xpath("//*[@id='pagination']/div[1]/div/div").click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pagination"]/div[1]/div/div/ul/li[4]/div'))).click()

time.sleep(3)

driver.find_element_by_class_name('container')
ai = driver.find_element_by_class_name('container')

b1 = ai.find_elements_by_class_name('debentures-list-item')

teste1lista = []
for tudo_deb in b1:
    teste1lista.append(tudo_deb.text)
    
final = []
for i in range(len(teste1lista)):
    final.append(teste1lista[i].split('\n')[0])

print(final)

df_final = pd.DataFrame(final)
df_final.to_csv('Nome_importado_anbima.csv', encoding='latin1')

driver.quit()
