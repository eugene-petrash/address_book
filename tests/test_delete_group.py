# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    old_groups_list = app.group.get_group_list()
    index = randrange(len(old_groups_list))
    app.group.delete_group_by_index(index)
    new_groups_list = app.group.get_group_list()
    assert len(old_groups_list) - 1 == app.group.count()
    old_groups_list[index:index+1] = []
    assert old_groups_list == new_groups_list


def test_delete_all_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    groups_list = app.group.get_group_list()
    app.group.delete_all_groups(groups_list)
    assert app.group.count() == 0