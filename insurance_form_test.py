import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class TestTricentis(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_enter_vehicle_data(self):
        driver = self.driver
        driver.get("http://sampleapp.tricentis.com/101/app.php")

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.title_contains("Enter Vehicle Data"))

        # Fill out the form
        vehicle_make = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "make")))
        select = Select(vehicle_make)
        select.select_by_visible_text("BMW")

        engineperformance = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "[kW]")))
        engineperformance.clear()
        engineperformance.send_keys("300")

        year = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "Date of Manufacture")))
        year.send_keys("2022")

        license_plate = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "License Plate Number")))
        license_plate.send_keys("BENZ-2022")

        annual_mileage = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "Annual Mileage")))
        annual_mileage.send_keys("5000")

        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "Next (Enter Insurant Data)")))
        next_button.click()

        # Wait for the next page to load
        WebDriverWait(driver, 10).until(EC.title_contains("Enter Insurant Data"))

        # Assert that the next page is the correct page
        assert "Insurance" in driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

