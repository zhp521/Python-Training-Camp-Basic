"""
测试练习: 集合操作
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.set_operations import student_set_operations

def test_student_set_operations():
    """测试学生集合操作函数"""
    # 初始学生集合
    math_club = {"张三", "李四", "王五"}
    coding_club = {"李四", "王五", "赵六"}
    
    # 测试集合并集
    result = student_set_operations(math_club, coding_club, "union")
    assert result == {"张三", "李四", "王五", "赵六"}
    
    # 测试集合交集
    result = student_set_operations(math_club, coding_club, "intersection")
    assert result == {"李四", "王五"}
    
    # 测试集合差集
    result = student_set_operations(math_club, coding_club, "difference")
    assert result == {"张三"} 