import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select #submodulo  para usar el dropdown

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_select_language(self):
        exposed_options=['English', 'French', 'German'] #Para almacenar las opciones que elijamos
        act_options=[]                                  #Para acceder a las opciones del dropdown

        select_language=Select(self.driver.find_element_by_id('select-language'))

        #Para comprobar que si esté la cantidad de  opciones correcta
        self.assertEqual(3,len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        #Verifico que la lista de opciones disponibles y activas sean indénticas
        self.assertListEqual(exposed_options,act_options)

        #Vamos a verificar la palabra "English" sea la primera opción seleccionada del dropdown
        self.assertEqual('English',select_language.first_selected_option.text)

        #Seleccionamos "German" por el texto visible
        select_language.select_by_visible_text('German')

        #Verificamos que el sitio cambio a Alemán
        self.assertTrue('store=german' in self.driver.current_url)

        #Preguntamos a selenium si la url del sitio contiene esas palabras
        select_language=Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity=2)