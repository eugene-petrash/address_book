from model.group import Group
import random
import string

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer3")
]


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