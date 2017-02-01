# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Test_1"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="Test_2"))
    app.session.logout()


def test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(footer="Test_3"))
    app.session.logout()
