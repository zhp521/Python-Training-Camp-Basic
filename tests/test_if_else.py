"""
测试练习: if-elif-else 条件语句
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.if_else import check_grade

def test_check_grade():
    """测试成绩等级判断函数"""
    # 测试优秀等级
    assert check_grade(95) == "优秀"
    assert check_grade(90) == "优秀"
    
    # 测试良好等级
    assert check_grade(89) == "良好"
    assert check_grade(80) == "良好"
    
    # 测试中等等级
    assert check_grade(79) == "中等"
    assert check_grade(70) == "中等"
    
    # 测试及格等级
    assert check_grade(69) == "及格"
    assert check_grade(60) == "及格"
    
    # 测试不及格等级
    assert check_grade(59) == "不及格"
    assert check_grade(0) == "不及格" 