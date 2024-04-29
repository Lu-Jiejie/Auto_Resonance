
from typing import List, Tuple, Union

def compare_ranges(
    low: Union['HSV', Tuple[int, int, int], List[int]],
    x: Union['HSV', Tuple[int, int, int], List[int]],
    high: Union['HSV', Tuple[int, int, int], List[int]],
):
    """
    说明:
        判断指定颜色是否在范围
    参数:
        :param low: 最低颜色
        :param x: 目标颜色
        :param high: 最高颜色
    """
    # 解构列表到单独的变量
    low_0, low_1, low_2 = low
    x_0, x_1, x_2 = x
    high_0, high_1, high_2 = high

    # 比较每个元素
    return (
        (low_0 <= x_0 <= high_0)
        and (low_1 <= x_1 <= high_1)
        and (low_2 <= x_2 <= high_2)
    )

class HSV:
    """HSV 模块"""

    def __init__(self, h: int, s: int, v: int, offset: int = 5):
        self.h = h
        self.s = s
        self.v = v
        self.offset = offset

    def __str__(self):
        return f"H: {self.h}, S: {self.s}, V: {self.v}"
    
    def __repr__(self):
        return f"HSV({self.h}, {self.s}, {self.v})"

    def __eq__(self, other: Union['HSV', Tuple[int, int, int], List[int]]):
        """
        说明:
            判断指定HSV是否在范围
        参数:
            :param other: 另一个 HSV
        :warning: 该方法会根据 offset 对前一个 HSV 进行范围偏移
        """
        return compare_ranges((self.h-self.offset, self.s-self.offset, self.v-self.offset), other, (self.h+self.offset, self.s+self.offset, self.v+self.offset))

    def __ne__(self, other: Union['HSV', Tuple[int, int, int], List[int]]):
        """
        说明:
            判断指定HSV是否不在范围
        参数:
            :param other: 另一个 HSV
        :warning: 该方法会根据 offset 对前一个 HSV 进行范围偏移
        """
        return not compare_ranges((self.h-self.offset, self.s-self.offset, self.v-self.offset), other, (self.h+self.offset, self.s+self.offset, self.v+self.offset))

    def __iter__(self):
        yield self.h
        yield self.s
        yield self.v
