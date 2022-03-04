import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_tee(self):                  #Busca elemento por nombre
        driver=self.driver
        search_field=driver.find_element_by_name('q')
        search_field.clear()                    #Limpia el campo de búsqueda en caso de que haya algún texto. 

        search_field.send_keys('tee')           #Simulamos la escritura del teclado para poner "tee"
        search_field.submit()                   #Envía los datos ('tee') para que la página muestre los resultados de "tee"

    def test_search_salt_shaker(self):
        driver=self.driver
        search_field=driver.find_element_by_name('q')
        
        search_field.send_keys('salt shaker')    #Escribimos 'salt shaker' en la barra de búsqueda
        search_field.submit()                    #Envíamos la petición

        #Hago una lista de los resultados buscando los elementos por su Xpath. Es la forma más rápida
        products=driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1,len(products))       #Revisa si la cantidad de productos es 1 o no 

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main(verbosity=2)