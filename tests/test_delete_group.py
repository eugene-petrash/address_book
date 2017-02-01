# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.delete_first_group()