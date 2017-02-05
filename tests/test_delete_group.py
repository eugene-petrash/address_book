# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_group(app):
    old_groups_list = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups_list = app.group.get_group_list()
    assert len(old_groups_list) - 1 == app.group.count()
    old_groups_list[0:1] = []
    assert old_groups_list == new_groups_list
