from dryad.markup.doctree import Node

class Root(Node):
    def __init__(self, child_nodes):
        self.child_nodes = list(child_nodes)

    doctree = ['child_nodes']
