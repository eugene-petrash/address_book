from model.group import Group


class GroupHelper():

    group_cache = None

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_all_groups(self, groups_list):
        wd = self.app.wd
        self.open_groups_page()
        index = 0
        for group in groups_list:
            group.index = index
            self.select_group_by_index(group.index)
            index += 1
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            is_present = len(wd.find_elements_by_name("selected[]"))
            if is_present > 0:
                for element in wd.find_elements_by_css_selector("span.group"):
                    text = element.text
                    id = element.find_element_by_name("selected[]").get_attribute("value")
                    self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
