# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups_list = app.group.get_group_list()
    new_group = Group(name="poiuytre", header="poiuy",
                                footer="poiuytre")
    app.group.create_group(new_group)
    new_groups_list = app.group.get_group_list()
    assert len(old_groups_list) + 1 == len(new_groups_list)
    old_groups_list.append(new_group)
    assert sorted(old_groups_list, key=Group.id_or_max) == \
           sorted(new_groups_list, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups_list = app.group.get_group_list()
    new_group = Group(name="", header="",
                      footer="")
    app.group.create_group(new_group)
    new_groups_list = app.group.get_group_list()
    assert len(old_groups_list) + 1 == len(new_groups_list)
    old_groups_list.append(new_group)
    assert sorted(old_groups_list, key=Group.id_or_max) == \
           sorted(new_groups_list, key=Group.id_or_max)