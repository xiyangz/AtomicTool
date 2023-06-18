from NodeGraphQt import BaseNode


class InputNode(BaseNode):
    """
    A node class with 0 inputs and 1 outputs.
    The last input and last output can take in multiple pipes.
    """

    # unique node identifier.
    __identifier__ = 'nodes.basic'

    # initial default node name.
    NODE_NAME = 'input node'

    def __init__(self):
        super().__init__()

        # create node inputs
        # self.add_output('multi out')
        self.add_input('multi in')