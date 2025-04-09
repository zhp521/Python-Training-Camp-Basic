"""
测试练习: 函数定义与参数
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.function_params import calculate_area

def test_calculate_area():
    """测试计算面积的函数"""
    # 测试长方形面积（提供两个参数）
    assert calculate_area(3, 4) == 12
    assert calculate_area(5, 6) == 30
    assert calculate_area(length=2, width=7) == 14
    
    # 测试正方形面积（只提供一个参数）
    assert calculate_area(5) == 25
    assert calculate_area(10) == 100
    assert calculate_area(length=4) == 16 