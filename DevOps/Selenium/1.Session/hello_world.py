import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:			#Va a ejecutar todo lo necesario para realizar una prueba
		cls.driver=webdriver.Chrome(executable_path= '/usr/bin/chromedriver')
		driver=cls.driver
		driver.implicitly_wait(10)
	
	def test_hello_world(self):			#Módulo de pruebas unitarias
		driver=self.driver
		driver.get('https://www.platzi.com')

	def test_visit_wikipedia(self):
		self.driver.get('https://www.wikipedia.org')
	
	@classmethod
	def tearDownClass(cls) -> None:			#Acciones de finalización, se cierran ventanas de navegador, etc
		cls.driver.quit()

if __name__=="__main__":				
	unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes',report_name='hello-world-report'))