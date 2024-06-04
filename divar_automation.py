import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

# Access the desired settings from the configuration file
car_brand = config.get('settings', 'car_brand')
desired_color_order = config.get('settings', 'desired_color_order')
maximum_price = config.getint('settings', 'maximum_price')
minimum_kilometrage = config.getint('settings', 'minimum_kilometrage')

def initialSetup():
    # Set up device emulation
    mobile_emulation = {
        "deviceName": "Pixel 2"
    }
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument('--start-maximized')
    

    # Initialize the Chrome WebDriver with mobile emulation
    driver = webdriver.Chrome(options=chrome_options)
    # Navigate to the Divar Tehran page
    driver.get("https://www.divar.ir/s/tehran")
    # Wait for the page to load
    time.sleep(1)
    return driver

def navigateToCarCategory(driver):
    # Click on the category menu
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/main/div[1]/div/div[2]').click()
    time.sleep(1)
    # Click on the car category 
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/main/div[1]/div/div[1]').click()
    time.sleep(1)
    # Click on passenger car subcatagory
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/main/div[1]/div/div[1]').click()
    time.sleep(1)
    return driver

def searchForSpecificVehicle(driver):
    # Find the search bar and enter the car brand
    search_bar = driver.find_element(By.XPATH, '/html/body/div/div[1]/header/nav/form/span[1]/div[2]/input')
    search_bar.send_keys(car_brand)
    search_bar.send_keys(Keys.RETURN)
    # Wait for the search results to load
    time.sleep(1)
    return driver

def navigateToFilterSection(driver):
    # Click on the filter button
    filter_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/header/nav/div/div/button')
    filter_button.click()
    time.sleep(1)

def filterByColor(driver):
    # Click on the color filter
    color_filter = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[3]')
    color_filter.click()
    time.sleep(1)
    # Open the color selection menu
    color_filter.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[4]/div/button').click()
    time.sleep(1)
    # Select the desired color based on the order
    color_selection = driver.find_element(By.XPATH, f"/html/body/div[6]/div/div/div/div/div/div[{desired_color_order}]")
    driver.execute_script("arguments[0].scrollIntoView(true);", color_selection)
    driver.execute_script("arguments[0].click();", color_selection)
    time.sleep(1)
    # Apply the selected color filter
    color_filter.find_element(By.XPATH, '/html/body/div[6]/div/div/div/footer/div/button[2]').click()
    time.sleep(1)
    return driver

def filterByMaximumPrice(driver):
    # Click on the price filter
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[7]').click()
    time.sleep(1)
    # Scroll to and click the price filter input field
    price_filter_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[8]/div/div/div[2]/div[2]/button')
    driver.execute_script("arguments[0].scrollIntoView(true);", price_filter_button)
    driver.execute_script("arguments[0].click();", price_filter_button)
    time.sleep(1)
    # Enter the maximum price and apply it
    price_filter_input = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[8]/div/div/div[2]/div[2]/div/div/div/input')
    price_filter_input.send_keys(maximum_price)
    price_filter_input.send_keys(Keys.RETURN)
    time.sleep(1)
    return driver

def filterByMinimumKilometrage(driver):
    # Click on the kilometrage filter
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[11]').click()
    time.sleep(1)
    # Scroll to and click the kilometrage filter input field
    kilometrage_filter_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[12]/div/div/div[2]/div[1]/button')
    driver.execute_script("arguments[0].scrollIntoView(true);", kilometrage_filter_button)
    driver.execute_script("arguments[0].click();", kilometrage_filter_button)
    time.sleep(1)
    # Enter the minimum kilometrage and apply it
    kilometrage_filter_input = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[12]/div/div/div[2]/div[1]/div/div/div/input')
    kilometrage_filter_input.send_keys(minimum_kilometrage)
    kilometrage_filter_input.send_keys(Keys.RETURN)
    time.sleep(1)
    return driver

def applyFilters(driver):
    # Click on the apply filters button
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/footer/div/button').click()
    time.sleep(1)
    return driver

def selectRandomResult(driver):
    # Find all search results
    results = driver.find_elements(By.CLASS_NAME, 'post-list__items-container-a9e81')
    print(len(results))
    # Select and click on a random result
    random_result = random.choice(results)
    random_result.click()
    return driver

def closeBrowser(driver):
    # Wait for a while before closing the browser
    time.sleep(5)
    driver.quit()

def main():
    # Initial setup of the WebDriver
    driver = initialSetup()
   
    # Navigate to the car category
    driver = navigateToCarCategory(driver)

    # Search for the specific vehicle
    driver = searchForSpecificVehicle(driver)
    
    # Navigate to the filter section
    navigateToFilterSection(driver)
    
    # Apply color filter
    driver = filterByColor(driver)

    # Apply maximum price filter
    driver = filterByMaximumPrice(driver)

    # Apply minimum kilometrage filter
    driver = filterByMinimumKilometrage(driver)

    # Apply all filters
    driver = applyFilters(driver)

    # Select a random result from the search results
    driver = selectRandomResult(driver)

    # Close the browser
    closeBrowser(driver)

if __name__ == "__main__":
    main()
