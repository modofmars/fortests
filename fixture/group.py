# -*- coding: utf-8 -*-


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


