import unittest
from selenium import webdriver
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://google.com')

    def test_browser_nav(self):
        driver=self.driver

        search_field=driver.find_element_by_name('q')
        search_field.clear()                        #Aseguramos que nuestra barra de busqueda esté limpia
        search_field.send_keys('platzi')            #Enviamos la palabra platzi para escribirla en la barra de busqueda
        search_field.submit()                       #Aceptamos

        driver.back()                               #Navega hacia atras una página
        sleep(3)                                    #Espera 3 segundos antes de realizar la siguiente actividad
        driver.forward()                            #Avanza la página
        sleep(3)
        driver.refresh()                            #Refresca el navegador
        sleep(3)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity=2)