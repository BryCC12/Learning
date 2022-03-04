import unittest
from selenium import webdriver
#sirve como excepción para los assertions cuando queremos validar la presencia de un elemento
from selenium.common.exceptions import NoSuchElementException
#Ayuda a llamar a las excepciones que queremos validar
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
    
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.NAME, 'select-language'))

    def tearDown(self):
        self.driver.quit()
        
    #Func para saber si está presente el elemento,        
    def is_element_present(self, how, what):                    #how: tipo de selector, #what: el valor que tiene
            try:
                self.driver.find_element(by=how, value=what)    #busca los elementos según el parámetro
            except NoSuchElementException is variable:
                return False
            return True

if __name__=="__main__":
    unittest.main(verbosity=2)