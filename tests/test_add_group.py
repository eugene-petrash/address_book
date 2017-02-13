# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    # prefix + random string with symbols from here^ + random len of the string
    return prefix + "-" + "".join([random.choice(symbols)
                             for i in range(random.randrange(maxlen))])

# specific scenarios with empty data + 5 scenarios with random data
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20),
          footer=random_string("footer", 20))
    for i in range (5)
]



@pytest.mark.parametrize("group", testdata, ids=[str(x) for x in testdata])
def test_add_group(app, group):
    old_groups_list = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_group_list()
    old_groups_list.append(group)
    assert sorted(old_groups_list, key=Group.id_or_max) == \
           sorted(new_groups_list, key=Group.id_or_max)


