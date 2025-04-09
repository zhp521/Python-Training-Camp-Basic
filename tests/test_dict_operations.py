"""
测试练习: 字典操作
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.dict_operations import student_dict_operations

def test_student_dict_operations():
    """测试学生字典操作函数"""
    # 初始学生字典
    initial_dict = {
        "张三": 85,
        "李四": 92,
        "王五": 78
    }
    
    # 测试添加学生
    result = student_dict_operations(initial_dict, "add", "赵六", 88)
    assert "赵六" in result
    assert result["赵六"] == 88
    
    # 测试删除学生
    result = student_dict_operations(result, "remove", "李四")
    assert "李四" not in result
    
    # 测试修改学生成绩
    result = student_dict_operations(result, "update", "张三", 95)
    assert result["张三"] == 95
    
    # 测试获取学生成绩
    score = student_dict_operations(result, "get", "张三")
    assert score == 95