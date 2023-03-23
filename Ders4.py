from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class test_Kodlama:
    def test_loginControl1(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")
         loginBtn = driver.find_element(By.ID, "login-button")
         loginBtn.click()
         errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
         testResult = errorMessage.text == "Epic sadface: Username is required"
         sleep(2)
         quit
    def test_loginControl2(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")
         sleep(1)
         usernameInput = driver.find_element(By.ID, "user-name")
         passwordInput = driver.find_element(By. ID,"password")
         sleep(1)
         usernameInput.send_keys("standard_user")
         passwordInput.send_keys("")
         loginBtn = driver.find_element(By.ID, "login-button")
         loginBtn.click()
         errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
         testResult = errorMessage.text == "Epic sadface: Password is required"
         print(f"{testResult}")
         sleep(2)
         quit
    def test_loginControl3(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")
         sleep(2)
         usernameInput = driver.find_element(By.ID, "user-name")
         passwordInput = driver.find_element(By. ID,"password")
         sleep(1)
         usernameInput.send_keys("locked_out_user")
         passwordInput.send_keys("secret_sauce")
         loginBtn = driver.find_element(By.ID, "login-button")
         loginBtn.click()
         errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
         testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
         print(f"{testResult}")
         sleep(2)
         quit
    def test_loginControl5(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")
         sleep(2)
         usernameInput = driver.find_element(By.ID, "user-name")
         passwordInput = driver.find_element(By. ID,"password")
         sleep(1)
         usernameInput.send_keys("standard_user")
         passwordInput.send_keys("secret_sauce")
         loginBtn = driver.find_element(By.ID, "login-button")
         loginBtn.click()
         listOfCourses = driver.find_elements(By.CLASS_NAME, "course-listing")
         sleep(2)
    def test_loginControl6(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")
         sleep(5)
         usernameInput = driver.find_element(By.ID, "user-name")
         passwordInput = driver.find_element(By. ID,"password")
         sleep(2)
         usernameInput.send_keys("standard_user")
         passwordInput.send_keys("secret_sauce")
         loginBtn = driver.find_element(By.ID, "login-button")
         loginBtn.click()
         productCount = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
         testResult = len(productCount) == 6
         sleep(2)
         print(f"İlgili sayfada {len(productCount)} adet ürün var.")
         
testClass = test_Kodlama()
testClass.test_loginControl1()
testClass.test_loginControl2()
testClass.test_loginControl3()        
testClass.test_loginControl5() 
testClass.test_loginControl6()      

