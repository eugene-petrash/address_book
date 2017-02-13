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

# Performance of all possible scenarios
testdata = [
    Group(name=name, header=header, footer=footer)
    # fill the field 'name' is empty or a random string with len 10 symbols
    for name in ["", random_string("name", 10)]
    # fill the field 'header' is empty or a random string with len 20 symbols
    for header in ["", random_string("header", 20)]
    # fill the field 'footer' is empty or a random string with len 25 symbols
    for footer in ["", random_string("footer", 25)]
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


