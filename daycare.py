class Daycare:
    def __init__(self, children, present_children, employees, parents):
        self.children = children
        self.present_children = present_children
        self.employees = employees
        self.parents = parents

    def check_in(self, child):
        if(child not in self.present_children):
            self.present_children.append(child)
        getattr(child, 'in_out_log').append("IN")

    def check_out(self, child):
        if(child in self.present_children):
            self.present_children.remove(child)
        getattr(child, 'in_out_log').append("OUT")

    def find_child(self):
        pass

    def authorize(self, employee_id, employees):
        if (employee_id in employees):
            return True
        else:
            return False

    def admin_features(self):
        pass
