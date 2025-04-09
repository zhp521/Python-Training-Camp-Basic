"""
测试练习: 列表操作
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.list_operations import student_list_operations

def test_student_list_operations():
    """测试学生列表操作函数"""
    # 初始学生列表
    initial_list = ["张三", "李四", "王五"]
    
    # 测试添加学生
    result = student_list_operations(initial_list, "add", "赵六")
    assert "赵六" in result
    assert len(result) == 4
    
    # 测试删除学生
    result = student_list_operations(result, "remove", "李四")
    assert "李四" not in result
    assert len(result) == 3
    
    # 测试修改学生
    result = student_list_operations(result, "update", "张三", "张小三")
    assert "张三" not in result
    assert "张小三" in result 