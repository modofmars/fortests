# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_fixber(app):
    app.session.login(username="ultras", password="KzkMK")
    app.group.edit_product_field(Group(product_kind="TeamCity Redmine Microsoft Visual Studio Python Python"))
    app.session.logout()


def test_fixber_another_data(app):
    app.session.login(username="ultras", password="KzkMK")
    app.group.edit_product_field(Group("rambler"))
    app.session.logout()
