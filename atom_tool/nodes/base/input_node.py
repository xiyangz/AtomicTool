from abc import ABCMeta, abstractclassmethod
from NodeGraphQt import BaseNode


class InputNode(BaseNode, metaclass=ABCMeta):
    """
    A node class with 0 inputs and 1 outputs.
    The last input and last output can take in multiple pipes.
    """

    # unique node identifier.
    __identifier__ = 'nodes.basic'

    # initial default node name.
    NODE_NAME = 'input node'

    def __init__(self, match_file_reg_exp, multi_input=True):
        super().__init__()
        # create node inputs
        self.add_input('multi in')

    @staticmethod
    def make_match_trace_file_reg_exp(trace_id: int) -> str:
        return ""
