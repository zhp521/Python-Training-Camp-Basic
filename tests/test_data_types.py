"""
测试练习: Python变量和数据类型
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.data_types import get_data_types

def test_get_data_types():
    """测试数据类型函数"""
    # 获取返回值
    result = get_data_types()
    
    # 检查是否为元组
    assert isinstance(result, tuple), "返回值应该是一个元组"
    
    # 检查元组长度
    assert len(result) == 4, "元组应该包含4个元素"
    
    # 检查每个元素的类型
    assert isinstance(result[0], int), "第一个元素应该是整数"
    assert isinstance(result[1], float), "第二个元素应该是浮点数"
    assert isinstance(result[2], str), "第三个元素应该是字符串"
    assert isinstance(result[3], bool), "第四个元素应该是布尔值"
    
    # 检查每个元素的值
    assert result[0] == 42, "整数值应该是42"
    assert result[1] == 3.14, "浮点数值应该是3.14"
    assert result[2] == "Python编程", "字符串值应该是'Python编程'"
    assert result[3] == True, "布尔值应该是True" 