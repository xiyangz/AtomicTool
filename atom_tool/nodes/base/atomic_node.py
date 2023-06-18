from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Optional, Dict
import pandas as pd
from NodeGraphQt import BaseNode


class AtomicNode(BaseNode, metaclass=ABCMeta):
    def __init__(self, node_name, icon):
        super().__init__()
        self.__init_ports()

    @abstractmethod
    def __init_ports(self):
        """
        初始化输入和输出节点信息
        """
        pass

    @abstractmethod
    def proc_data(self, input_data_frames: Dict[str, pd.DataFrame]) -> Dict[str, Optional[pd.DataFrame]]:
        """
        处理输入的数据，返回结果
        :param input_data_frames: 格式为 {input_port_name: data_frame, ...}
        :return: 格式为 {output_port_name: data_frame, ...}, 意外情况return {output_port_name: None, ...}
        """
        pass

    @abstractmethod
    def verify_output(self, output_data_frames: Optional[Dict[str, pd.DataFrame]]) -> bool:
        pass
