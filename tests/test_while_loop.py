"""
测试练习: while循环
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.while_loop import find_first_even

def test_find_first_even():
    """测试查找第一个偶数的函数"""
    # 测试列表中有偶数的情况
    assert find_first_even([1, 2, 3, 4, 5]) == 2
    assert find_first_even([7, 9, 10, 13]) == 10
    assert find_first_even([2, 4, 6, 8]) == 2
    
    # 测试列表中没有偶数的情况
    assert find_first_even([1, 3, 5, 7, 9]) is None
    
    # 测试空列表
    assert find_first_even([]) is None 