import unittest
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path= '/usr/bin/chromedriver')
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):                  #Busca elemento por ID
        search_field=self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):           #Busca elemento por nombre
        search_field=self.driver.find_element_by_name("q")

    def test_search_text_field_by_class(self):          #Busca elemento por clase
        search_field=self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):               #Busca elemento por clase - botón
        button=self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):        #Genera una lista de las imagenes
        banner_list=self.driver.find_element_by_class_name("promos")
        banners=banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3,len(banners))

    def test_vip_promo(self):                           #Encuentra item por XPath
        vip_promo=self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def test_shopping_cart(self):                       #Encuentra icono por medio de CSS Selector
        shopping_cart_icon=self.driver.find_element_by_css_selector('div.header-minicart span.icon')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main(verbosity=2)