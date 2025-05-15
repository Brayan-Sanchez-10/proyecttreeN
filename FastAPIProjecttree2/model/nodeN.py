from model.person import Person

class NodeN:
    def __init__(self, data: Person):
        self.data = data
        self.parent = None

    def set_parent(self, parent_node):
        self.parent = parent_node

