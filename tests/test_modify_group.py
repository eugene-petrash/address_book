# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    old_groups_list = app.group.get_group_list()
    index = randrange(len(old_groups_list))
    modify_group = Group(name="Test_1")
    modify_group.id = old_groups_list[index].id
    app.group.modify_group_by_index(modify_group, index)
    assert len(old_groups_list) == app.group.count()
    new_groups_list = app.group.get_group_list()
    old_groups_list[index]= modify_group
    assert sorted(old_groups_list, key=Group.id_or_max) == \
           sorted(new_groups_list, key=Group.id_or_max)


# def test_modify_group_header(app):
#     old_groups_list = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="Test_2"))
#     new_groups_list = app.group.get_group_list()
#     assert len(old_groups_list) == len(new_groups_list)
#
#
# def test_modify_group_footer(app):
#     old_groups_list = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="Test_3"))
#     new_groups_list = app.group.get_group_list()
#     assert len(old_groups_list) == len(new_groups_list)