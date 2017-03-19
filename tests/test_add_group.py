# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, data_groups):
    group = data_groups
    old_groups_list = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_group_list()
    old_groups_list.append(group)
    assert sorted(old_groups_list, key=Group.id_or_max) == \
           sorted(new_groups_list, key=Group.id_or_max)
