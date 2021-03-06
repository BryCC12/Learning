import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_new_user(self):
        driver=self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a').click()
        #le decimos al driver que encuentre la opción de cuenta por su Xpath y le haga click para desplegar el menu
        driver.find_element_by_link_text('Log In').click()
        #El driver va a buscar el enlace por su texto y haga click
        
        create_account_button=driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        #creo una variable asociada al botón de crear cuenta
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        #validamos que el botón esté visible y habilitado
        create_account_button.click()

        self.assertEqual('Create New Customer Account',driver.title)
        #comprueba que estamos en el sitio de crear cuenta
        
        #Creación de variables con el nombre del selector correspondiente
        first_name=driver.find_element_by_id('firstname')
        middle_name=driver.find_element_by_id('middlename')
        last_name=driver.find_element_by_id('lastname')
        email_address=driver.find_element_by_id('email_address')
        news_letter_suscription=driver.find_element_by_id('is_subscribed')
        password=driver.find_element_by_id('password')
        confirm_password=driver.find_element_by_id('confirmation')
        submit_button=driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        #Veremos si los elementos están habilitados con send_keys()
        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_suscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())

        #Mandamos los datos al formulario
        first_name.send_keys('Test')
        driver.implicitly_wait(1)
        middle_name.send_keys('Test')
        driver.implicitly_wait(1)
        last_name.send_keys('Test')
        driver.implicitly_wait(1)
        email_address.send_keys('Test@gmail.com')
        driver.implicitly_wait(1)
        password.send_keys('Test')
        driver.implicitly_wait(1)
        confirm_password.send_keys('Test')
        driver.implicitly_wait(1)
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity=2)
