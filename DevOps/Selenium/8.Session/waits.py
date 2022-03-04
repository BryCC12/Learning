import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By #Herramienta para seleccionar elementos de la web con sus selectores
from selenium.webdriver.support.ui import WebDriverWait #Herramienta para hacer uso de las expected conditions y esperas explicitas
from selenium.webdriver.support import expected_conditions as EC    #Importar esperar explicitas

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_account_link(self):        #Cuentas del sitio
        #Esperar 10 segundos hasta que se cumpla la funcion
        WebDriverWait(self.driver,10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length')=='3')

        #Hacer referencia al enlace donde estan las cuentas
        account=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

    def test_create_new_customer(self): #Creacion de nuevo usuario
        #Encontrar el elemento por el texto del enlace
        self.driver.find_element_by_link_text('ACCOUNT').click()

        #Hacer referencia a la cuenta
        my_account=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'My Account')))
        my_account.click()

        #Referencia a crear una cuenta
        create_account_button=WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.LINK_TEXT,'CREATE AN ACCOUNT')))
        create_account_button.click()

        #Verificacion de estado de pagina web
        WebDriverWait(self.driver,10).until(EC.title_contains('Create New Customer Account'))


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity=2)