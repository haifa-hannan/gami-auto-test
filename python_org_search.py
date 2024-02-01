import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # --- The Keys class provides keys in the keyboard like RETURN, F1, ALT etc. ----
from selenium.webdriver.common.by import By # --- The By class is used to locate elements within a document. ---

# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn ("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn ("No Results found.", driver.page_source)

    def tearDown(self):    
        self.driver.close()

if __name__ == "__main__":
    unittest.main()