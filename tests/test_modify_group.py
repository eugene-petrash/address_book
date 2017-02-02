# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    old_groups_list = app.group.get_group_list()
    app.group.modify_first_group(Group(name="Test_1"))
    new_groups_list = app.group.get_group_list()
    assert len(old_groups_list) == len(new_groups_list)


def test_modify_group_header(app):
    old_groups_list = app.group.get_group_list()
    app.group.modify_first_group(Group(header="Test_2"))
    new_groups_list = app.group.get_group_list()
    assert len(old_groups_list) == len(new_groups_list)


def test_modify_group_footer(app):
    old_groups_list = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="Test_3"))
    new_groups_list = app.group.get_group_list()
    assert len(old_groups_list) == len(new_groups_list)