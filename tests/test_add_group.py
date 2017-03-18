# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.add_group import testdata
# from data.add_group import constant as testdata


@pytest.mark.parametrize("group", testdata, ids=[str(x) for x in testdata])
def test_add_group(app, group):
    old_groups_list = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_group_list()
    old_groups_list.append(group)
    assert sorted(old_groups_list, key=Group.id_or_max) == \
           sorted(new_groups_list, key=Group.id_or_max)
