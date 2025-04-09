"""
测试练习: break和continue语句
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.break_continue import skip_multiples_of_three

def test_skip_multiples_of_three():
    """测试跳过3的倍数的函数"""
    # 测试正常情况
    assert skip_multiples_of_three(10) == [1, 2, 4, 5, 7, 8, 10]
    assert skip_multiples_of_three(5) == [1, 2, 4, 5]
    
    # 测试边界情况
    assert skip_multiples_of_three(3) == [1, 2]
    assert skip_multiples_of_three(1) == [1]
    assert skip_multiples_of_three(0) == [] 