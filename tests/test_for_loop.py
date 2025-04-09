"""
测试练习: for循环
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.for_loop import sum_numbers

def test_sum_numbers():
    """测试计算整数和的函数"""
    # 测试常规情况
    assert sum_numbers(1) == 1
    assert sum_numbers(5) == 15  # 1+2+3+4+5=15
    assert sum_numbers(10) == 55  # 1+2+...+10=55
    assert sum_numbers(100) == 5050  # 等差数列求和公式: n*(n+1)/2
    
    # 测试边界情况
    assert sum_numbers(0) == 0 