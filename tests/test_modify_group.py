# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="Test_1"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="Test_2"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="Test_3"))