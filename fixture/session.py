# -*- coding: utf-8 -*-


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
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

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_id("TB_overlay").click()
        wd.find_element_by_css_selector("img.pic").click()
        wd.find_element_by_xpath("//div[@class='ad']/div[6]/a/img").click()

