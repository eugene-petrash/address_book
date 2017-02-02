# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups_list = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups_list = app.group.get_group_list()
    assert len(old_groups_list) - 1 == len(new_groups_list)
