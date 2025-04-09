"""
测试练习: 使用math模块
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.math_module import calculate_square_root

def test_calculate_square_root():
    """测试计算平方根的函数"""
    # 测试完全平方数
    assert calculate_square_root(0) == 0.0
    assert calculate_square_root(1) == 1.0
    assert calculate_square_root(4) == 2.0
    assert calculate_square_root(9) == 3.0
    assert calculate_square_root(16) == 4.0
    assert calculate_square_root(25) == 5.0
    
    # 测试非完全平方数
    assert calculate_square_root(2) == pytest.approx(1.414, 0.001)
    assert calculate_square_root(3) == pytest.approx(1.732, 0.001)
    assert calculate_square_root(5) == pytest.approx(2.236, 0.001) 