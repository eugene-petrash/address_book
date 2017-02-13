# -*- coding: utf-8 -*-
from model.group import Group
import pytest


# specific scenarios
testdata = [
    Group(name="poiuytre-1", header="poiuy-1", footer="poiuytre-1"),
    Group(name="poiuytre-2", header="poiuy-2", footer="poiuytre-2"),
    Group(name="poiuytre-3", header="poiuy-3", footer="poiuytre-3"),
    Group(name="poiuytre-4", header="poiuy-4", footer="poiuytre-4"),
    Group(name="", header="", footer="")]


@pytest.mark.parametrize("group", testdata, ids=[str(x) for x in testdata])
def test_add_group(app, group):
    old_groups_list = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_group_list()
    old_groups_list.append(group)
    assert sorted(old_groups_list, key=Group.id_or_max) == \
           sorted(new_groups_list, key=Group.id_or_max)


