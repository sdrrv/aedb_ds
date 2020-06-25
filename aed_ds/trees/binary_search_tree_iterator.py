from ..stacks.list_stack import ListStack


class Iterator():
    def __init__(self, root):
        self.stack = ListStack()
        setup()

    def setup(self):
        current_node = root
        while current_node != None:
            self.stack.push(root)
            current_node = current_node.get_left_child()

    def has_next(self):
        return self.stack.size() != 0

    def next(self):
        next_node = self.stack.pop()
        current_node = next_node.get_right_child()
        while current_node != None:
            self.stack.push(current_node)
            current_node = current_node.get_left_child()
        return next_node.get_element()
