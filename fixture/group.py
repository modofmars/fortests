# -*- coding: utf-8 -*-
import time

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def edit_product_field(self, Group):
        wd = self.app.wd
        # open user setting page
        wd.find_element_by_xpath("//div[@id='TB_ajaxContent']/div/input").click()
        wd.find_element_by_css_selector("img.pic").click()
        # edit product field
        wd.find_element_by_name("product_kind").click()
        wd.find_element_by_name("product_kind").clear()
        wd.find_element_by_name("product_kind").send_keys(Group.product_kind)
        # submit changing
        wd.find_element_by_xpath("//form[@id='form']/table/tbody/tr[38]/td[1]/input[3]").click()

    def add_skills(self):
        wd = self.app.wd
        # open user setting page
        wd.find_element_by_xpath("//div[@id='TB_ajaxContent']/div/input").click()
        wd.find_element_by_css_selector("img.pic").click()
        wd.find_element_by_link_text("опыт и навыки").click()
        if not wd.find_element_by_name("c42").is_selected():
            wd.find_element_by_name("c42").click()
        if not wd.find_element_by_name("c100").is_selected():
            wd.find_element_by_name("c100").click()
        if not wd.find_element_by_name("c58").is_selected():
            wd.find_element_by_name("c58").click()
        if not wd.find_element_by_name("c83").is_selected():
            wd.find_element_by_name("c83").click()
        if not wd.find_element_by_name("c37").is_selected():
            wd.find_element_by_name("c37").click()
        if not wd.find_element_by_name("c32").is_selected():
            wd.find_element_by_name("c32").click()
        if not wd.find_element_by_name("c35").is_selected():
            wd.find_element_by_name("c35").click()
        if not wd.find_element_by_name("c5").is_selected():
            wd.find_element_by_name("c5").click()
        if not wd.find_element_by_name("c25").is_selected():
            wd.find_element_by_name("c25").click()
        if not wd.find_element_by_name("c26").is_selected():
            wd.find_element_by_name("c26").click()
        if not wd.find_element_by_name("c18").is_selected():
            wd.find_element_by_name("c18").click()
        if not wd.find_element_by_name("c96").is_selected():
            wd.find_element_by_name("c96").click()
        if wd.find_element_by_name("c96").is_selected():
            wd.find_element_by_name("c96").click()
        if not wd.find_element_by_name("c50").is_selected():
            wd.find_element_by_name("c50").click()
        if not wd.find_element_by_name("c90").is_selected():
            wd.find_element_by_name("c90").click()
        wd.find_element_by_xpath("//form[@id='form']/table/tbody/tr[3]/td[1]/input[4]").click()
