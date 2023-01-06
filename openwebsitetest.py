import unittest
from xmlrunner import XMLTestRunner
from selenium import webdriver

class TestWebpage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_title(self):
        self.driver.get("https://www.tricentis.com")
        actual_title = self.driver.title
        expected_title = "wrong title"
        self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}' but got '{actual_title}'")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    with open("test_results.xml", "w") as f:
        runner = XMLTestRunner(f)
        unittest.main(testRunner=runner)
