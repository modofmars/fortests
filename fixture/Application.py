# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def destroy(self):
        self.wd.quit()

    def logout(self):
        # logout
        wd = self.wd
        wd.find_element_by_id("TB_overlay").click()
        wd.find_element_by_css_selector("img.pic").click()
        wd.find_element_by_xpath("//div[@class='ad']/div[6]/a/img").click()

    def edit_product_field(self, Group):
        wd = self.wd
        # open user setting page
        wd.find_element_by_xpath("//div[@id='TB_ajaxContent']/div/input").click()
        wd.find_element_by_css_selector("img.pic").click()
        # edit product field
        wd.find_element_by_name("product_kind").click()
        wd.find_element_by_name("product_kind").clear()
        wd.find_element_by_name("product_kind").send_keys(Group.product_kind)
        # submit changing
        wd.find_element_by_xpath("//form[@id='form']/table/tbody/tr[38]/td[1]/input[3]").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_css_selector("li").click()
        wd.find_element_by_link_text("Вход").click()
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys(username)
        wd.find_element_by_xpath("//form[@id='form']/table[2]/tbody/tr/td[1]/table/tbody/tr[5]/td").click()
        wd.find_element_by_name("passw").click()
        wd.find_element_by_name("passw").clear()
        wd.find_element_by_name("passw").send_keys(password)
        wd.find_element_by_name("btn").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://fixber.com/")
