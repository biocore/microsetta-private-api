from microsetta_private_api.model.vue.vue_group import VueGroup
from microsetta_private_api.model.vue.vue_schema import VueSchema


class VueFactory:
    def __init__(self):
        self.fields = []
        self.groups = []
        self.active_fields = []
        self.active_legend = None

    def add_field(self, field):
        if self.active_legend is None:
            self.fields.append(field)
        else:
            self.active_fields.append(field)
        return self

    def start_group(self, legend):
        if self.active_legend is not None:
            raise Exception("Group already active")
        if legend is None:
            raise Exception("Cannot start group with legend==None")
        self.active_legend = legend
        return self

    def end_group(self):
        new_group = VueGroup(self.active_legend, self.active_fields)
        self.groups.append(new_group)
        self.active_fields = []
        self.active_legend = None
        return self

    def build(self):
        return VueSchema(self.groups, self.fields)
