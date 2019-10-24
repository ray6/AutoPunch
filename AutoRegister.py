# Generated by Selenium IDE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class AutoRegister():
    def __init__(self, method="signin"):
        self.vars = {}
        self.driver = webdriver.Firefox()
        self.url = "url"
        self.username = "username"
        self.passwd = "passwd"
        self.LogInPortal()
        self.goRegisterPage()
        if method == "signin":
            self.autoSignIn()
        else:
            self.autoSignOut()

    def teardown_method(self):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def LogInPortal(self):
        self.driver.get(self.url)
        self.driver.set_window_size(1206, 696)
        self.driver.find_element(By.ID, "userid_input").send_keys(self.username)
        self.driver.find_element(By.NAME, "j_password").send_keys(self.passwd)
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    def goRegisterPage(self):
        self.vars["window_handles"] = self.driver.window_handles
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'人事系統 / Human System')]"))).click()
        self.vars["win271"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win271"])
        elem = self.driver.find_element_by_xpath("//nav/ul/li[1]")
        hover = ActionChains(self.driver).move_to_element(elem)
        hover.perform()
        elem2 = self.driver.find_element_by_xpath("//nav/ul/li[1]/ul/li[2]/a")
        hover2 = ActionChains(self.driver).move_to_element(elem2).click(elem2)
        hover2.perform()
        del elem, elem2, hover, hover2
        for i in range(2, 6):
            path_check = "//*[@id='table1']/tbody/tr[" + str(i) + "]/td[contains(text(), '工讀：1081資工系辦工讀生')]"
            # css_select = "tr:nth-child("+str(i)+") .btn:nth-child(1)"
            path_select = "//*[@id='table1']/tbody/tr[" + str(i) + "]/td[6]/a[contains(text(), '新增簽到')]"
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, path_check)))
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, path_select))).click()
                break
            except:
                pass

    def autoSignIn(self):
        print("signIn")
        self.driver.find_element(By.ID, "signin").click()
        self.teardown_method()

    def autoSignOut(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "AttendWork"))).send_keys("協助系辦工作")
        self.driver.find_element(By.ID, "signout").click()
        self.close_windows()
        self.teardown_method()
