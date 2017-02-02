# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups_list = app.group.get_group_list()
    app.group.create_group(Group(name="poiuytre", header="poiuy",
                                footer="poiuytre"))
    new_groups_list = app.group.get_group_list()
    assert len(old_groups_list) + 1 == len(new_groups_list)


def test_add_empty_group(app):
    old_groups_list = app.group.get_group_list()
    app.group.create_group(Group(name="", header="",
                      footer=""))
    new_groups_list = app.group.get_group_list()
    assert len(old_groups_list) + 1 == len(new_groups_list)