# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    old_groups_list = app.group.get_group_list()
    modify_group = Group(name="Test_1")
    modify_group.id = old_groups_list[0].id
    app.group.modify_first_group(modify_group)
    new_groups_list = app.group.get_group_list()
    assert len(old_groups_list) == len(new_groups_list)
    old_groups_list[0]= modify_group
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