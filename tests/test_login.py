# -*- coding: utf-8 -*-

from model.group import Group


def test_fixber(app):
    app.group.edit_product_field(Group(product_kind="TeamCity Redmine Microsoft Visual Studio Python Python"))


def test_fixber_another_data(app):
    app.group.edit_product_field(Group("rambler"))
    app.session.logout()
