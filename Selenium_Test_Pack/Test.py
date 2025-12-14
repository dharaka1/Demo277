from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.save_screenshot("main_page.png")
Search_Product= wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@title="Search for Products, Brands and More"]')))
Search_Product.send_keys("Sony tv",Keys.ENTER)
driver.save_screenshot("Search_Product.png")
Scroll_Into_Product=wait.until(EC.visibility_of_element_located((By.XPATH,'//div[text()="SONY 80 cm (32 inch) HD Ready LED Smart Google TV"]')))
driver.execute_script("arguments[0].scrollIntoView();",Scroll_Into_Product)
driver.save_screenshot("Scroll_Into_Product.png")


Click_Into_Product=wait.until(EC.visibility_of_element_located((By.XPATH,'//div[text()="SONY BRAVIA 2 II 189.3 cm (75 inch) Ultra HD (4K) LED Smart Google TV 2025 Edition"]')))
Click_Into_Product.click()
driver.save_screenshot("Click_Into_Product.png")

Original_Window=driver.window_handles
driver.switch_to.window(Original_Window[1])


Scroll_Into_Cart=wait.until(EC.visibility_of_element_located((By.XPATH,'//div[text()="Questions and Answers"]')))
driver.execute_script("arguments[0].scrollIntoView();",Scroll_Into_Cart)
driver.save_screenshot("Scroll_Into_Cart.png")

Click_Cart=wait.until(EC.visibility_of_element_located((By.XPATH,'//button[text()="Add to cart"]')))
Click_Cart.click()
driver.save_screenshot("Click_Cart.png")

Assert_page=wait.until(EC.visibility_of_element_located((By.XPATH,'//a[text()="SONY BRAVIA 2 II 189.3 cm (75 inch) Ultra HD (4K) LED Smart Google TV 2025 Edition"]'))).text

try:
    assert True
    print("Test case Passed")
except AssertionError:
    print("Test case Failed")
driver.save_screenshot("Assert_page.png")

time.sleep(10)
driver.quit()
