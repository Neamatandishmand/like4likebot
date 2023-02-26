from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

class Like4LikeAutomation():
    def like4like(self):
        # launch the browser and like4like website
        PATH = "C:\program Files\chromedriver.exe"
        driver = webdriver.Chrome(service=Service(PATH))
        driver.get("https://www.like4like.org/#social-media-platform-list")
        driver.maximize_window()

        # hit the login
        login = driver.find_element(By.XPATH, "//a[@title='Login ']")
        login.click()

        #provide username
        username = driver.find_element(By.XPATH, "//input[@id='username']")
        username.send_keys("username")
        #  providing password
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys("password")
        # hit enter
        password.send_keys(Keys.RETURN)
        time.sleep(10)

        # clicking the free link
        free = driver.find_element(By.XPATH, "//ul[@class='font-book']//li//a[text()='Free']")
        free.click()

        # selecting the feature
        driver.implicitly_wait(30)
        select_twitter_like = driver.find_element(By.XPATH, "//option[@value='twitterfav']")
        select_twitter_like.click()

        #  hit the like button
        parent_handler = driver.current_window_handle
        like_button = driver.find_element(By.CSS_SELECTOR, "div[id^='likebutton']")
        like_button.click()
        driver.implicitly_wait(50)
        # switch the window
        all_hander = driver.window_handles
        print("type of all hendler",type(all_hander))

        for handle in all_hander:
            if handle != parent_handler:
                driver.switch_to.window(handle)
                driver.implicitly_wait(100)
                time.sleep(5)
                print("this is the child url: ", driver.current_url)
                driver.find_element(By.XPATH, "//span[text()='Log in']").click()
                driver.implicitly_wait(100)
                email = driver.find_element(By.XPATH, "//input[@name='text']")

                email.send_keys("your email")
                email.send_keys(Keys.RETURN)
                driver.implicitly_wait(100)
                f_password = driver.find_element(By.XPATH, "//input[@name='password']")
                f_password.send_keys("your password")
                f_password.send_keys(Keys.RETURN)
                driver.implicitly_wait(300)
                time.sleep(30)
                like = driver.find_element(By.XPATH, "//div//div[@data-testid='like']")
                driver.implicitly_wait(100)
                like.click()
                time.sleep(5)
                print("one tweet liked!")
                driver.implicitly_wait(400)
                driver.close()
                driver.switch_to.window(parent_handler)
                confirm = driver.find_element(By.XPATH, "//img[@title='Click On The Button To Confirm Interaction!']")
                confirm.click()
                break

        list = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                32, 33, 34, 35, 36, 37, 38, 39, 40]
        count = 0
        for li in list:
            like_button = driver.find_element(By.CSS_SELECTOR, "div[id^='likebutton']")
            like_button.click()
            driver.implicitly_wait(100)
            a_handle = driver.window_handles
            try:
                for handle in a_handle:
                    if handle != parent_handler:
                        driver.switch_to.window(handle)
                        driver.implicitly_wait(100)
                        time.sleep(5)
                        print("this is the child url: ", driver.current_url)
                        driver.find_element(By.XPATH, "//span[text()='Log in']").click()
                        driver.implicitly_wait(100)
                        email = driver.find_element(By.XPATH, "//input[@name='text']")

                        email.send_keys("your email")
                        email.send_keys(Keys.RETURN)
                        driver.implicitly_wait(100)
                        f_password = driver.find_element(By.XPATH, "//input[@name='password']")
                        f_password.send_keys("yout password")
                        f_password.send_keys(Keys.RETURN)
                        driver.implicitly_wait(300)
                        time.sleep(5)
                        like = driver.find_element(By.XPATH, "//div//div[@data-testid='like']")
                        driver.implicitly_wait(100)
                        like.click()
                        time.sleep(5)
                        print("one tweet liked!")
                        driver.implicitly_wait(400)
                        driver.close()
                        driver.switch_to.window(parent_handler)
                        confirm = driver.find_element(By.XPATH, "//img[@title='Click On The Button To Confirm Interaction!']")
                        confirm.click()
            except:
                for handle in a_handle:
                    count += 1
                    if handle != parent_handler:
                        driver.switch_to.window(handle)

                        driver.implicitly_wait(90)
                        time.sleep(2)
                        like = driver.find_element(By.XPATH, "//div[@aria-label='Like'][@role='button'][@tabindex='0']")
                        driver.implicitly_wait(10)
                        like.click()
                        print("You liked ", count, " tweets")
                        time.sleep(2)
                        driver.implicitly_wait(400)
                        driver.close()
                        driver.switch_to.window(parent_handler)
                        time.sleep(1)
                        confirm = driver.find_element(By.XPATH, "//img[@title='Click On The Button To Confirm Interaction!']")
                        confirm.click()
                        time.sleep(5)
#
#
Like4LikeObject = Like4LikeAutomation()
Like4LikeObject.like4like()