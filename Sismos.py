#!/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(executable_path= './chromedriver')
browser.maximize_window()
browser.get('http://www2.ssn.unam.mx:8080/catalogo/')

time.sleep(4)


# string_prov = 'select[name="ctl00$ContentPlaceHolder1$DropDownListProvincia"] option[value="38"]'
# desplegable_prov = browser.find_element_by_css_selector(string_prov)
# click = desplegable_prov.click()
# time.sleep(4)



#agregar_estacion = browser.find_element_by_css_selector('input[name="ctl00$ContentPlaceHolder1$ButtonAgregar"]')
#click_estacion = agregar_estacion.click()
# time.sleep(7)

# TEXTO
# browser.find_element_by_id("txtFechaIni").clear()
# time.sleep(1)

inputElement = browser.find_element_by_id("initialDate")
inputElement.send_keys('2022-03-02')
time.sleep(2)


select = Select(browser.find_element_by_name("states"))
select.select_by_value('GRO')
time.sleep(5)


WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]'))).click()
vibility_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="inputType"]')))
time.sleep(5)

#inputElement = browser.find_element_by_id('txtFechaFin')
# inputElement.send_keys('15/11/2018')
# time.sleep(3)

#browser.find_element_by_xpath('//*[@id="inputType"]').submit()
if vibility_element == True:
    browser.find_element_by_xpath('//*[@id="inputType"]').click()
else:
    print('no entro')

# Descargar excel
#browser.find_element_by_css_selector("button.btn btn-default.btn-action.btn-download-csv.text-uppercase")

# browser.switch_to.window(browser.window_handles[1])
#exportar_csv_link = browser.find_element_by_css_selector('a[id="ContentPlaceHolder1_ExportarCSV"]')
#descargar_csv = exportar_csv_link.click()
# time.sleep(5)
# browser.quit()

# zip_ref=zipfile.ZipFile(get_download_path()+'/InformeDatos.zip','r')
# zip_ref.extractall("Resultados/")
# zip_ref.close()
